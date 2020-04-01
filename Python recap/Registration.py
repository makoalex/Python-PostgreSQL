def create_student(mark):

    user_input_first = input(' enter the first name please:\n')
    user_input_last = input('enter the last name please\n')
    student = {'FirstName': user_input_first,
               'LastName': user_input_last,
               'Marks': []

               }

    def marks():

        student['Marks'].append(mark)
        return student

    print(marks())


def calculate_average(mark):
    create_student(mark)
    if len(mark) == 0:
        raise ValueError("can't divide  by 0")
    total = sum(mark)
    average = total / len(mark)
    return 'The total score is {}, and the average grade is {}:'.format( total, average)

def student_details()

print(calculate_average([6.46, 8]))
