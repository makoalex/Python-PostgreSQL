def game(magic_num):
    user_input = input('please guess\n')

    if user_input in magic_num:
        print('won')
    else:
        print('wrong')

    again = ['y', 'n']
    answer = ''
    while answer not in again:
        answer = input(' wanna have another go? y/n')
    if answer in again[0]:
        return game(magic_num)
    else:
        print('bye')


game(["3", "9"])
