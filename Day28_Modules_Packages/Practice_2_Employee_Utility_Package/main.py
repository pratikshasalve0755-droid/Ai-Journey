from employee.details import get_employee_details , show_employee_details
from employee.salary import get_salary_details , calculate_salary

emp_id , name , dept , designation = get_employee_details()
print("------------------------------------")
basic_salary , bonus = get_salary_details()

print("\n------- Employee Details --------")
show_employee_details(emp_id , name ,  dept , designation)

print("\n-------- Employee Salary ---------")
final_salary = calculate_salary(basic_salary , bonus)
print(f"Final Salary : {final_salary}")