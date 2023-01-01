class Appointment:
    """A class that deals with the Appointment operations"""

    def __init__(self, doctor, patient, year, month, day, status):
        """
        Args:
            doctor (string): Doctor's full name
            patient (string): Patient's full name
            year (string): Year of appointment eg. 2023
            month (string): Month of appointment eg. Jan
            day (string): Day of appointment eg. 23
            status (string): Status of appointment eg. Approved or Pending
        """

        self.__doctor = doctor
        self.__patient = patient
        self.__year = year
        self.__month = month
        self.__day = day
        self.__status = status

    def get_patient(self):
        return self.__patient

    def get_doctor(self):
        return self.__doctor

    def get_month(self):
        return self.__month

    def get_status(self):
        return self.__status

    def get_date(self):
        return f"{self.__month} {self.__day}, {self.__year}"

    def to_json(self):
        return {
            "doctor": self.__doctor,
            "patient": self.__patient,
            "year": self.__year,
            "month": self.__month,
            "day": self.__day,
            "status": self.__status
        }

    def __str__(self):
        return f'{self.get_patient():^30}|{self.get_doctor():^30}|{self.get_date():^20}|{self.get_status():^10}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __o: object) -> bool:
        return self.__class__ == __o.__class__ and self.__repr__() == __o.__repr__()
