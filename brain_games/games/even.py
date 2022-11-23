from random import randint
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def games():
    number = randint(1, 20)
    if number % 2 == 0:
        correct_answer = 'yes'
    elif number % 2 != 0:
        correct_answer = 'no'
    return number, correct_answer
