from .Admin import Admin
from .Appointment import Appointment
from .Patient import Patient
from .Doctor import Doctor


def admin_fromJson(json: dict) -> 'Admin':
    return Admin(username=json["username"], password=json["password"], address=json["address"])


def appointment_fromJson(json: dict) -> 'Appointment':
    return Appointment(doctor=json["doctor"], patient=json["patient"], year=json["year"], month=json["month"], day=json["day"], status=json["status"])


def doctor_fromJson(json: dict) -> 'Doctor':
    return Doctor(first_name=json["first_name"], surname=json["surname"], speciality=json["speciality"])


def patient_fromJson(json: dict) -> 'Patient':
    return Patient(first_name=json["first_name"], surname=json["surname"], age=json["age"], mobile=json["mobile"], postcode=json["postcode"], symptoms=json["symptoms"], doctor=json["doctor"])
