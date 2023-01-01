# Imports
import app


def main():
    """
    the main function to be ran when the program runs
    """

    db = app.DatabaseManager(database="app/database/database.json")

    # Initialising the actors
    patient = db.get(0, table="patients", map_func=app.patient_fromJson)

    while True:
        # print the menu
        print('Choose the operation:')
        print(' 1- Book an appointment')
        print(' 2- View assigned doctor')
        print(' 3- View appointments')
        print(' 4- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Book an appointment
            patient.book_appointment(db)

        elif op == '2':
            # 2- View assigned doctor
            patient.view_assigned_doctor(db)

        elif op == '3':
            # 3- View appointments
            patient.view_appointments(db)

        elif op == '4':
            # 4 - Quit
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
