# try
# except
# else
# finally

game = True
while game is True:
    try:
        num = int(input('please enter a number\n'))
    except ValueError:
        print("That's not a number")
    else:
        print('{} is a great number'.format(num))
        print('This is printed if the exception does not occur.')
        game = False
    finally:
        print('This gets printed all the time, no matter what.')


# another example
def exponentiation():
    try:
        number1 = int(input('enter a number '))
        number2 = int(input('enter the number '))
        result = number1 ** number2
    except TypeError as err:
        print('Must be an integer')
        print(err)
    except ValueError as err:
        print('wrong input')
        print('Error type', err)
    else:
        print('{} raised by the power of {} is {}'.format(number1, number2, result))


exponentiation()
