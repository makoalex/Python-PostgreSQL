# asking the user for input
import requests

url = "https://api.norsk-tipping.no/LotteryGameInfo/v1/api/results/lotto?fromDate=2019-12-16&toDate=2020-03-31"


def get_data():
    global winning_numbers
    result = requests.get(url, headers={'Accept': 'application/json'})
    response = result.json()
    data = response['gameResult'][0]['winnerNumber']
    print(data)
    winning_numbers = set([int(e['number']) for e in data])
    return winning_numbers


def user():
    get_data()
    user_input = input(' please enter 6 numbers between 1 and 45 separated by commas\n')
    input1 = list(map(int, user_input.split(',')))
    user_input1 = set(input1)

    def check_input():
        if len(user_input1) > 6:
            print('too many numbers')
        elif len(user_input1) < 6:
            print('need more numbers')
        else:
            print('The number you chose are: {} '.format(user_input1))
            final_result = winning_numbers.intersection(user_input1)
            int_result = len(final_result)
            print('congratulations you have {} matching numbers: {}'. format(int_result, final_result))

    check_input()


user()
