# Program 2: Student Result Analyzer
print("\nProgram 2: Student Result Analyzer")

marks = [ 35, 67, 89, 42, 28, 76, 91, 33]
grades = ["A" if m >= 90 else "B" if m>=75  else "C" if m >=60 else "D" if m >=50 else "F" for m in marks if m >=40 ]
passed = [ x for  x in marks if x >= 40 ]
failed = [ i for i in marks if i < 40]


print(f"\n Marks: {marks}")
print(f" Passed: {passed}")
print(f" Grades: {grades}")
