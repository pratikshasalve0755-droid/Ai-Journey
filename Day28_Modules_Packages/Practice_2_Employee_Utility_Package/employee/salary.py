def get_salary_details():
    basic_salary =int(input("Basic Salary:"))
    bonus = int(input("Bonus:"))
    return basic_salary , bonus


def calculate_salary(basic_salary , bonus):
    print(f"Basic Salary:{basic_salary}")
    print(f"Bonus:{bonus}")
    final_salary = basic_salary + bonus
    return final_salary


