# Program 2: Teacher and Subject System
print("Program 2: Teacher and subject System")

class Teacher:
    def __init__(self , name):
        self.name = name
        self.subjects_list = []

    def add_subject(self , subject):
        self.subjects_list.append(subject)

    def display(self):
        print(f"Teacher Name : {self.name}")
        if not  self.subjects_list:
            print("subject not assigned yet!")

        else:
            for s in self.subjects_list:
                print(f"Subjects: {s}" )


class SubjectManager:
    def __init__(self):
        self.teachers_list =  {}

    def add_teacher(self):
        t_name = input("Enter Name:").strip()
        if not t_name:
            print("Name is required!")
            return

        self.teachers_list[t_name] = Teacher(t_name)
        print("Teacher name added successfully!")

    def assign_subject(self):
        t_name = input("Enter Name:").strip()

        if t_name not in self.teachers_list:
            print(f"{t_name} teacher not found!")

        sub_name = input("Enter subject name:").strip()
        self.teachers_list[t_name].add_subject(sub_name)
        print("Subject assigned successfully!")

    def view_teacher_subjects(self):
        if not self.teachers_list:
            print("Teacher not found!")

        print("--- List of Teachers ---")
        for t in self.teachers_list.values():
                t.display()

        print("-------------------")


    def main_menu(self):
        while True:
            print("\nSelect Option")
            print("1. Add Teacher")
            print("2. Assign Subject")
            print("3. View Teacher-Subjects")
            print("4. Exit")
            print("--------------------------")
            try:
                choice = int(input("Enter Your Choice:"))
            except ValueError:
                print("Invalid Value!")
                continue

            if choice == 1:
                self.add_teacher()

            elif choice == 2:
                self.assign_subject()

            elif choice == 3:
                self.view_teacher_subjects()

            elif choice == 4:
                print("Exit!")
                break
            else:
                print("Invalid Choice!")

manager = SubjectManager()
manager.main_menu()
