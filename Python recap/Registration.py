def create_student():
    user_input_first = input(' enter the first name please:\n')
    user_input_last = input('enter the last name please\n')
    student = {'FirstName': user_input_first,
               'LastName': user_input_last,
               'Marks': []

               }

    def marks():
        #nonlocal student
        student['Marks'].append(5)
        return student
    print(marks())
create_student()