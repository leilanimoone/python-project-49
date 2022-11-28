from random import randint, choice
TASK = 'What is the result of the expression?'


def generator():
    signs = ['+', '-', '*']
    first_number = randint(15, 30)
    second_number = randint(1, 15)
    sign = choice(signs)
    number = f'{first_number} {sign} {second_number}'
    if sign == '+':
        correct_answer = first_number + second_number
    elif sign == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return number, str(correct_answer)
