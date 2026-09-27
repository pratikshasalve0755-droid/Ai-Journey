#Program 3: Open Non-Existing  File
print("\nProgram 3: Open Non-Existing  File")

while True:
 try:
    file_name = input("\nEnter file name:-")
    with open( file_name , "r" , newline="") as  file:
        print(f"File {file_name} Opened succesfully!")
        print("File found  succesfully!")

 except FileNotFoundError:
    print(f"File {file_name} not found!\ncreate file {file_name} first! ")
