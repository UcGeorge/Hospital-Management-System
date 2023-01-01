# Imports
from app.database.database_manager import *
import app.models as models


class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def full_name(self):
        return f"{self.get_first_name()} {self.get_surname()}"

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    # def add_patient(self, patient):
    #     self.__patients.append(patient)

    # def remove_patient(self, patient):
    #     self.__patients.remove(patient)

    def get_len_assigned_patients(self, db: DatabaseManager):
        return len(db.get_where('patients', lambda p: p.get_doctor(
        ) == self.full_name(), models.patient_fromJson)[0])

    def get_len_appointments_for_month(self, db: DatabaseManager, month: str):
        return len(db.get_where('appointments', lambda a: a.get_doctor(
        ) == self.full_name() and a.get_month().lower().startswith(month.lower()), models.appointment_fromJson)[0])

    def view_assigned_patients(self, db: DatabaseManager):

        patients = db.get_where('patients', lambda p: p.get_doctor(
        ) == self.full_name(), models.patient_fromJson)[0]

        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def view_appointments(self, db: DatabaseManager):

        appointments = db.get_where('appointments', lambda a: a.get_doctor(
        ) == self.full_name(), models.appointment_fromJson)[0]

        print("-----Appointments-----")
        print(
            f'ID |{"Patient":^30}|{"Doctor":^30}|{"Appointment Date":^20}|{"Status":^10}')
        self.view(appointments)

    def to_json(self):
        return {
            "first_name": self.__first_name,
            "surname": self.__surname,
            "speciality": self.__speciality,
        }

    def __str__(self):
        return f'{self.full_name():^30}|{self.get_speciality():^15}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __o: object) -> bool:
        return self.__class__ == __o.__class__ and self.__repr__() == __o.__repr__()
