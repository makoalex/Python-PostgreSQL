class Student:
    student_list = []

    def __init__(self, student, mark):
        self.student = student
        self.mark = mark

    def create_student(self, student):
        student= input('please enter your name\n').lower().strip()
        self.student = {'Name': student,
                        'Marks': []}


class Registration(Student):
    def __init__(self):
        super().__init__()

    def adding_student(self):
        return Student.student_list.append(self.adding_marks)

    def adding_marks(self, mark):
        self.student['Marks'].append(mark)
        return self.student

    def calculate_average(self):
        if len(self.student['Marks']) == 0:
            raise ValueError("can't average with 0 values")
        total = sum(self.student['Marks'][0])
        average = total / len(self.student['Marks'])
        return average

    def student_details(self):
        return '{} and the average is {}'.format(self.student['Name'], self.calculate_average())

    def getting_all_list(self):
        for element, self.student in enumerate(Student.student_list):
            print('ID: {}'.format(element))
            print(self.student_details())

    def menu_settings(self):
        selection = input("Enter:\n"
                          "'p' to get the student list \n"
                          "'s'to add a new  student,\n"
                          "'a' to add a new mark to a student,\n"
                          "'q' to quit\n"
                          "Enter selection:\n")
        # while selection != 'q':
        if selection == 'p':
            print(self.getting_all_list())
        elif selection == 's':
            print(Student.student_list.append(self.adding_student()))
        elif selection == 'a':
            student_id = int(input("Enter the student id to add a mark to:\n"))
            self.student = Student.student_list[student_id]
            new_mark = int(input("Enter the new mark to be added"))
            self.adding_marks(new_mark)


s = Registration()
print(s.menu_settings())
