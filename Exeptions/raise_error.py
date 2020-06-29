def make_color(text, colour):
    available_colours = ('cyan', 'yellow', 'magenta', 'blue')
    if type(text) is not str:
        raise TypeError('text has to be instance of string')
    if colour not in available_colours:
        raise ValueError('colour not available for use')
    if type(colour) is not str:
        raise ValueError('colour must be an instance of str')
    print('printed {} in {}'.format(text, colour))


make_color('hey there', 'orange')
make_color('hei','yelloww')

"""helpful for making custom error messages, raise our own type error"""
