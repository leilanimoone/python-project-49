import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    elif number % 2 != 0:
        correct_answer = 'no'
    return correct_answer


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 3
    for _ in range(attempts):
        number = randint(1, 20)
        correct_answer = is_even(number)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(.'
                f' Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
