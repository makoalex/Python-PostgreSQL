def game(magic_num):
    user_input = int(input('please guess\n'))

    def repeat():
        again = ['y', 'n']
        answer = ''
        while answer not in again:
            answer = input(' wanna have another go? y/n')
        if answer in again[0]:
            return game(magic_num)
        else:
            print('bye')

    if user_input in magic_num:
        print('won')
    else:
        print('wrong')
        return repeat()


game([3,9])
