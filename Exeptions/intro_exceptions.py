Number = input('enter a number')
try:
    print(int(Number) * 2)
except ValueError:
    print('You did not enter a base 10 number')
print('hello world')

""" the try and except block is used to catch exceptions """
# Python executes as normal the code following try.
# the exceptions determines how the program responds to exceptions
# when the exception occurs, the program will continue and not crash
