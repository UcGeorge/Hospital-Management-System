# Imports
from app.database.database_manager import *
import app.models as models


class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """

        print("-----Login-----")
        # Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if self.__username == username and self.__password == password:
            return self.__username
        else:
            return None

    def find_index(self, index, doctors):

        # check that the doctor id exists
        if index in range(0, len(doctors)):

            return True

        # if the id is not in the list of doctors
        else:
            return False

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')

        return first_name, surname, speciality

    def doctor_management(self, db: DatabaseManager):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Option: ")

        doctors = db.get_all('doctors', models.doctor_fromJson)

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break  # save time and end the loop

            if name_exists:
                return

            # add the doctor ...
            db.insert('doctors', models.Doctor(
                first_name, surname, speciality))
            # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index != False:

                        break

                    else:
                        print("Doctor not found")

                        # doctor_index is the ID mines one (-1)

                except ValueError:  # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ').lower()  # make the user input lowercase

            # First name
            if op == '1':
                first_name = input('Enter the first name: ')
                doctors[index].set_first_name(first_name)
                print('Doctor\'s first name updated.')

            # Surname
            elif op == '2':
                surname = input('Enter the surname: ')
                doctors[index].set_surname(surname)
                print('Doctor\'s surname updated.')

            # Speciality
            elif op == '3':
                speciality = input('Enter the speciality: ')
                doctors[index].set_speciality(speciality)
                print('Doctor\'s speciality updated.')

            # if the op is not in the list of operations
            else:
                print('Invalid operation choosen. Check your spelling!')

            db.update('doctors', index, doctors[index])

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            try:
                # doctor_index is the ID minus one (-1)
                index = int(
                    input('Enter the ID of the doctor to be deleted: ')) - 1
                doctor_index = self.find_index(index, doctors)
                if doctor_index != False:

                    if db.delete('doctors', index, models.doctor_fromJson):
                        print("Doctor deleted sucessfully.")
                    else:
                        print("Failed to delete doctor.")

                else:
                    print("Doctor not found")

            except ValueError:  # the entered id could not be changed into an int
                print('The ID entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, db: DatabaseManager):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """

        patients = db.get_all('patients', models.patient_fromJson)

        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, db: DatabaseManager):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """

        patients = db.get_all('patients', models.patient_fromJson)
        doctors = db.get_all('doctors', models.doctor_fromJson)

        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()  # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors) != False:
                patients[patient_index].link(doctors[doctor_index].full_name())

                db.update('patients', patient_index, patients[patient_index])

                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, db: DatabaseManager):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        patients = db.get_all("patients", models.patient_fromJson)

        print("-----Discharge Patient-----")

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(input('Please enter the patient ID: ')) - 1

            if self.find_index(patient_index, patients) != False:

                db.insert('discharged_patients', db.delete(
                    'patients', patient_index, models.patient_fromJson))

                print('The patient is now discharged.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')

    def view_discharge(self, db: DatabaseManager):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        discharged_patients = db.get_all(
            "discharged_patients", models.patient_fromJson)

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
        pass

    def update_details(self, db: DatabaseManager):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            self.__username = input('Enter the new username: ')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            self.__address = input('Enter the new address: ')

        else:
            print('Invalid operation choosen.')

        db.update('admin', 0, self)

    def len_where(self, a_list: list, where):
        count = 0
        for a in a_list:
            if where(a):
                count += 1
        return count

    def view_management_report(self, db: DatabaseManager):

        patients = db.get_all('patients', models.patient_fromJson)
        doctors = db.get_all('doctors', models.doctor_fromJson)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        def number_of_patients_per_doctor(d): return self.len_where(
            patients, where=lambda p: p.get_doctor() == d.full_name())

        print("-----Management Report-----")
        print(f"Total number of doctors in the system: {len(doctors)}")
        print("---------------------------------------------------------------")
        print(f"Total number of patients & appointments per month per doctor:")
        print(
            f'ID |{"Doctor":^30}|{"Num of Patients":^17}|{"Appointments ->":^17}|{"|".join(list(map(lambda m: f"{m:^5}", months)))}')
        for index, doc in enumerate(doctors):
            print(f'{index+1:3}|{doc.full_name():^30}|{doc.get_len_assigned_patients(db):^17}|{"":^17}|{"|".join(list(map(lambda m: f"{doc.get_len_appointments_for_month(db,m):^5}", months)))}')
        print("---------------------------------------------------------------")
        print(f"Total number of patients in the system: {len(patients)}")
        print("---------------------------------------------------------------")

    def to_json(self):
        return {
            "username": self.__username,
            "password": self.__password,
            "address": self.__address
        }

    def __repr__(self) -> str:
        return self.__username

    def __eq__(self, __o: object) -> bool:
        return self.__class__ == __o.__class__ and self.__repr__() == __o.__repr__()
