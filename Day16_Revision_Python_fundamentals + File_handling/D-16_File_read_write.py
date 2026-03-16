#Program 3:File_Read_Write -Practice
print("\nProgram 3: File_Read_Write.py")

lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)


story = '\n'.join(lines)
with open("BTS_Arirang_Story.txt" , "w" , newline='') as file :
    file.write(story)

print("The story is Saved to the BTS_Arirang_Story.txt file ")

with open ("BTS_Arirang_Story.txt" , "r" ) as file:
   print("\n Saved Story:- " , file.read())

