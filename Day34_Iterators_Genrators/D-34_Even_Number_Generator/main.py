# Program 3: Even Number Generator
print("Program 3: Even Number Generator")



def even_generator():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i

gen = even_generator()
while True:
    try:
       print(next(gen))

    except StopIteration:
        print("Even Numbers Generate Successfully!")
        break