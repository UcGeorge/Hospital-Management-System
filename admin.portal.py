# Imports
import app


def main():
    """
    the main function to be ran when the program runs
    """

    db = app.DatabaseManager(database="app/database/database.json")

    # Initialising the actors
    # username is 'admin', password is '123'
    admin = db.get(0, table="admin", map_func=app.admin_fromJson)

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True  # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- View management report')
        print(' 7- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(db)

        elif op == '2':
            # 2- View or discharge patients
            admin.view_patient(db)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(db)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')

        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(db)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(db)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details(db)

        elif op == '6':
            # 6- View management report
            admin.view_management_report(db)

        elif op == '7':
            # 7 - Quit
            raise KeyboardInterrupt()

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')


if __name__ == '__main__':
    print("-----Admin Portal-----")
    try:
        main()
    except KeyboardInterrupt:
        print("Closing application.")
    # except:
    #     print("Closing application due to an unhandled exception.")
