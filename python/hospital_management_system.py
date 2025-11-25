# The project will be a simple Hospital Management System using Flask and SQLite.
# Our logic will live here

# Relationship: A department can have multiple doctors and nurses.
# Import a class for regex operations ie email format validations
import re



class Patient:
    # Attributes
    def __init__(self, name, age, gender, address, phone_number, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.appointments = []



    # Method to get patient details
    def get_details(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Address": self.address,
            "Phone Number": self.phone_number,
            "Email": self.email
        }

    # Age validation method: Age should be a positive integer
    def validate_age(self):
        if isinstance(self.age, int) and self.age > 0:
            return True
        return False

    #Method to update patient information
    def update_info(self, age = None, name = None, gender = None, address = None, phone_number = None, email = None):
        """
        It is important to understand that by using age = None, name = None etc in the method parameters we are making the parameters optional.
        :param age:
        :param name:
        :param gender:
        :param address:
        :param phone_number:
        :param email:
        :return:
        """
        if age is not None:
            self.age = age
        if name is not None:
            self.name
        if gender is not None:
            self.gender = gender
        if address is not None:
            self.address = address
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email

    # Method to validate email format
    def validate_email_format(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, self.email):
            return True
        return False

    # Method to validate patient data
    def validate_data(self):
        if not self.validate_age():
            return False
        if not isinstance(self.name, str) or self.name.strip() == "":
            return False
        if not self.validate_email_format():
            return False
        return None

    # Method to schedule appointments: Maximum 3 appointments per day
    def schedule_appointment(self, doctor, date, time, reason):
        # We have to check for the doctors availablity and if we have not exceeded the maximum appointments per day for the patient.




    # Method to cancel appointments
    def cancel_appointment(self, appointment):
        # Check if the appointment exists for the patient and cancel it.
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            return True
        return False

    # Method to reschedule appointments
    def cancel_appointment(self, appointment, new_date, new_time):
    # Check if the appointment exists for the patient and reschedule it.
        if appointment in self.appointments:
            appointment.date = new_date()
            appointment.time = new_time()
        return True

    # Method to check appointment status (boolean)
    def check_appointment_status(self, appointment):
        return appointment in self.appointments


    # Method to display patient information
    def display_info(self):
        info = self.get_details()
        for key, value in info.items():
            print(f"{key} : {value}")

class Doctor:
    # Attributes
    def __init__(self, name, age, specialty, phone_number,email):
        self.name = name
        self.age = age
        self.specialty = specialty
        self.phone_number = phone_number
        self.email = email

    # Method to get doctor details



    # Age validation method: Age should be a positive integer and be above 25



    # Method to update doctor information



    # Method to validate doctor data



    # Method to schedule availability slots: Maximum appointments per daya should not exceed 10



    # Method to display doctor information




class Nurse:
    def __init__(self, name, age, speciality, phone_number, email):
        self.name = name
        self.age = age
        self.speciality = speciality
        self.phone_number = phone_number
        self.email = email




class Department:
    def __init__(self, name, floor, head):
        self.name = name
        self.floor = floor
        self.head = head
        self.doctors = []
        self.nurses = []


        # Methods to add doctors and nurses to the department, ensure to keep count




        # Method to remove doctors and nurses from the departments




        # Method to list all doctors and nurses in the department


        # Method to get department details


        # Method to update department information




        # Method to validate department data



        # Method to display department information





class Appointment:
    def __init__(self, patient, doctor, date, time, reason):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.reason = reason



        # Method to schedule an appointment: Ensure not to double-book doctors and patients




        # Method to cancel an appointment




        # Method to reschedule an appointment





        # Method to check appointment status (boolean)





        # Method to send appointment reminders via email or SMS




        # Method to update appointment details



        # Method to check for conflicts with other appointments



        # Method to display appointment details, we can use the __str__method for this.




