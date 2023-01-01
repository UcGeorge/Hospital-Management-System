# Imports
from app.database.database_manager import *
import app.models as models


class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms, doctor=None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode (string): postcode
            symptoms (list): Symptoms
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__doctor = doctor if doctor else 'None'

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

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        print("-----Patient Symptoms-----")
        self.view(self.__symptoms)

    def book_appointment(self, db: DatabaseManager):
        print("-----Book Appointment-----")
        # Get the details of the appointment

        year = input('Enter the year: ')
        month = input('Enter the month: ')
        day = input('Enter the day: ')

        appointment = models.Appointment(doctor="", patient=self.full_name(
        ), year=year, month=month, day=day, status="Pending")
        db.insert('appointments', appointment)

        print(f"Appointment booked for {appointment.get_date()}.")

    def view_assigned_doctor(self, db: DatabaseManager):
        print("-----Assigned Doctor-----")

        docs = db.get_where('doctors', lambda d: d.full_name()
                            == self.get_doctor(), models.doctor_fromJson)[0]

        print('ID |          Full name           |  Speciality')
        self.view(docs)

    def view_appointments(self, db: DatabaseManager):
        print("-----Appointments-----")

        appointments = db.get_where('appointments', lambda a: a.get_patient()
                                    == self.full_name(), models.appointment_fromJson)[0]

        print(
            f'ID |{"Patient":^30}|{"Doctor":^30}|{"Appointment Date":^20}|{"Status":^10}')
        self.view(appointments)

    def to_json(self):
        return {
            "first_name": self.__first_name,
            "surname": self.__surname,
            "age": self.__age,
            "mobile": self.__mobile,
            "postcode": self.__postcode,
            "symptoms": self.__symptoms,
            "doctor": self.__doctor
        }

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __o: object) -> bool:
        return self.__class__ == __o.__class__ and self.__repr__() == __o.__repr__()
