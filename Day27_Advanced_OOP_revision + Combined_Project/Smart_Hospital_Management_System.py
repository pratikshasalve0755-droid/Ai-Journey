# Mini Project: Smart Hospital Management System
print("Mini Project: Smart Hospital Management System")


from abc import ABC, abstractmethod
class HospitalStaff(ABC):
    def __init__(self , staff_id, name):
        self.__staff_id = staff_id
        self.name = name

    @abstractmethod
    def work(self):
        pass

    def get_staff_details(self):
        return (f"Staff ID : {self.__staff_id}\n"
                f"Staff Name : {self.name}")


class Doctor(HospitalStaff):
    def __init__(self ,staff_id , name , specialization):
        super().__init__(staff_id , name)
        self.specialization = specialization

    def work(self):
        return f"The Doctor Treating patients!"

    def get_staff_details(self):
        parent_details = super().get_staff_details()
        return (f"{parent_details}\n"
        f"Specialization : {self.specialization}")


class Nurse(HospitalStaff):
    def __init__(self , staff_id , name , shift):
        super().__init__(staff_id, name)
        self.shift = shift

    def work(self):
        return "The Nurse assists the patients!"

    def get_staff_details(self):
        parent_details = super().get_staff_details()
        return (f"{parent_details}\n"
            f"Shift : {self.shift} ")

class Receptionist(HospitalStaff):
    def __init__(self ,staff_id , name  , desk_no):
        super().__init__(staff_id , name)
        self.desk_no = desk_no

    def work(self):
        return "Receptionist is managing appointments."
    def get_staff_details(self):
        parent_details = super().get_staff_details()
        return (f"{parent_details}\n"
                f"Desk No. : {self.desk_no}")

doctor = Doctor("D101" , "Dr. Shraddha Gaikwad" , "Cardiologist")
nurse = Nurse("N205" , "Rutuja k." , "Day Shift")
recep = Receptionist("R303" , "Neha A" , 5)

staff_members = [doctor , nurse , recep]

for staff in staff_members:
    print("\n-----------------------------------------")
    print(staff.get_staff_details())
    print(staff.work())




