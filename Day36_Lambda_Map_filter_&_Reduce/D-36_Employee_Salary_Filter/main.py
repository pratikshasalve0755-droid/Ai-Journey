#Program 2: Employee Salary Filter
print("\nProgram 2: Employee Salary Filter")


salary = [18000, 35000, 42000, 15000, 50000]

highest_salary = list(filter(lambda x:  x > 30000 , salary))
print("\nSalary Greater than 30000:" , highest_salary )
