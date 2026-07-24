# Program 2 : Number Generator
print("\nProgram 2: Number Generator")

start_number = int(input("\nEnter Start Number : "))
end_number = int(input("Enter End Number : "))

def generate_numbers(start_number, end_number):
    for num in range(start_number , end_number +1):
        yield num

gen = generate_numbers(start_number , end_number)

while True:
    try:
       print(next(gen))

    except StopIteration:
       print("All numbers generated successfully.!")
       break
