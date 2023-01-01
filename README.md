# Objective

The partial code that is provided contains the following classes. You are given partial functions that allow the following tasks of the Admin class. For the Doctor and Patient, you are given partial functions that do some of the following tasks.

Admin

- Admin Login
- Register/view/update/delete doctor
- View patients
- Can assign doctor to patient

Doctor

- View their patient details assigned to them by admin
- View their appointments

Patient

- Apply to be admitted to the hospital
- Book an appointment
- View the assigned doctor
- Check the status of their appointment (approved, pending, or denied)

The application **must** implement all the above and the following:

Create the necessary classes and functions which allow admins to perform the following tasks:

- Discharge a patient account Le. remove patient from the system when the treatment is done
- Admins can view the discharged patient list
- Update admin own information i.e. name and address

The application **must** implement all the above and the following:

- Patients have names, symptoms, age, mobile, address etc.
- Patients of the same family are grouped together by Admin
- The hospital system should be able to store and load all patients' data from and into a file

The application **must** implement all the above and the following:

- Relocating patients from one doctor to another.
- Admins can request a management report. This should show the following information:
    1. Total number of doctors in the system
    2. Total number of patients per doctor
    3. Total number of appointments per month per doctor
    4. Total number of patients based on the illness type.
