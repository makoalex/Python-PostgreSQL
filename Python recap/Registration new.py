import pickle

class Student:
    student_list = []

    def __init__(self):
        name = input('please enter your name\n').lower().strip()
        self.student = {'Name': name,
                   'Marks': []}



class Registration:
    def __init__(self):
        pass


    def adding_student(self):
        return Student.student_list.append(self.adding_marks)

    def adding_marks(self,mark, student):
        student.student['Marks'].append(mark)
        return student

    def calculate_average(self, student):
        if len(student.student['Marks'])== 0:
            raise ValueError("can't average with 0 values")
        total = sum(student.student['Marks'])
        average = total / len(student.student['Marks'])
        return average

    def student_details(self, student):
        return '{} and the average is {}'.format(student.student['Name'], self.calculate_average(student))

    def getting_all_list(self):
        for element, student in enumerate(Student.student_list):
            print('ID: {}'.format(element))
            print(self.student_details(student))

    def save_students_to_file(self, name):
        pickle.dump(Student.student_list, open(name, "wb"))

    def open_students_from_file(self, name):
        Student.student_list = pickle.load(open(name,"rb"))

    def menu_settings(self):
        keep_running = True
        while keep_running:
            selection = input("Enter:\n"
                              "'p' to get the student list \n"
                              "'s'to add a new  student,\n"
                              "'a' to add a new mark to a student,\n"
                              "'q' to quit\n"
                              "'l' to load\n"
                              "'w' to save\n"
                              "Enter selection:\n")
            if selection == 'p':
                print(self.getting_all_list())
            elif selection =='s':
                print(Student.student_list.append(Student()))
            elif selection == "w":
                name = input("Enter filename")
                self.save_students_to_file(name)
                print("File stored")
            elif selection == "l":
                name = input("Enter filename")
                self.open_students_from_file(name)
                print("File loaded")
            elif selection == 'a':
                student_id = int(input("Enter the student id to add a mark to:\n"))
                student = Student.student_list[student_id]
                new_mark = float(input("Enter the new mark to be added"))
                self.adding_marks(new_mark,student)
            elif selection == 'q':
                keep_running = False




s = Registration()
s.menu_settings()