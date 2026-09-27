def get_employee_details():
     print()
     emp_id = input("Employee ID:")
     name = input("Name:")
     dept = input("Department:")
     designation = input("Designation:")

     return emp_id , name , dept , designation

def show_employee_details(emp_id , name , dept , designation):

     print(f"Employee ID: {emp_id}")
     print(f"Name:{name}")
     print(f"Department:{dept}")
     print(f"Designation:{designation}")




