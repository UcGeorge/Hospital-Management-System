import json


class Transaction:
    def __init__(self, database: str) -> None:
        self.__database = database
        self.__snapshot = None

    def __enter__(self):
        # Open the JSON file
        with open(self.__database, 'r') as database:
            # Load the JSON data into a Python dictionary
            self.__snapshot = json.load(database)

        # The data is now stored in the `data` dictionary
        return self.__snapshot

    def __exit__(self, *args):
        # Open a file for writing
        with open(self.__database, "w") as database:
            # Write the dictionary to the file as JSON
            json.dump(self.__snapshot, database)


class DatabaseManager:
    def __init__(self, database: str) -> None:
        self.__database = database

    def get(self, index, table, map_func):
        record = None
        with Transaction(self.__database) as snapshot:
            try:
                record = snapshot[table][index]
            except:
                print(
                    f"An error occoured while getting record at index {index} from {table}")

        return map_func(record) if record else None

    def get_all(self, table, map_func):
        table_list = []
        with Transaction(self.__database) as snapshot:
            try:
                for record in snapshot[table]:
                    table_list.append(map_func(record))
            except:
                print(f"An error occoured while getting records from {table}")

        return table_list

    def get_where(self, table, where, map_func):
        table_list = []
        indexes = []

        with Transaction(self.__database) as snapshot:
            try:
                for index, record in enumerate(snapshot[table]):
                    obj = map_func(record)
                    if where(obj):
                        table_list.append(obj)
                        indexes.append(index)
            except:
                print(f"An error occoured while getting records from {table}")

        return table_list, indexes

    def insert(self, table, json_serialisable_object):
        success = False
        with Transaction(self.__database) as snapshot:
            try:
                snapshot[table].append(json_serialisable_object.to_json())
                success = True
            except:
                print(f"An error occoured while inserting record to {table}")

        return success

    def delete(self, table, index, map_func):
        record = None
        with Transaction(self.__database) as snapshot:
            try:
                record = snapshot[table].pop(index)
            except:
                print(f"An error occoured while deleting record from {table}")

        return map_func(record) if record else None

    def update(self, table, index, json_serialisable_object):
        success = False
        with Transaction(self.__database) as snapshot:
            try:
                snapshot[table][index] = json_serialisable_object.to_json()
                success = True
            except:
                print(f"An error occoured while deleting record from {table}")

        return success
