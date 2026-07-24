# Program 1: Student Roll Iterator
print("\nProgram 1: Student Roll Iterators")


stu_roll_no = [101 , 102 , 103 , 104 , 105]

iterator = iter(stu_roll_no)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

except StopIteration:
   print("All roll numbers displayed.")



