# Imports
import app


def main():
    """
    the main function to be ran when the program runs
    """

    db = app.DatabaseManager(database="app/database/database.json")

    # Initialising the actors
    doctor = db.get(0, table="doctors", map_func=app.doctor_fromJson)

    while True:
        # print the menu
        print('Choose the operation:')
        print(' 1- View patients assigned by admin')
        print(' 2- View appointments')
        print(' 3- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- View patients assigned by admin
            doctor.view_assigned_patients(db)

        elif op == '2':
            # 2- View appointments
            doctor.view_appointments(db)

        elif op == '3':
            # 3 - Quit
            raise KeyboardInterrupt()

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')


if __name__ == '__main__':
    print("-----Doctor Portal-----")
    try:
        main()
    except KeyboardInterrupt:
        print("Closing application.")
    # except:
    #     print("Closing application due to an unhandled exception.")
