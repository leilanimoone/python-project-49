from random import randint
task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def games():
    number = randint(2, 100)
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
        divisor += 1
    return number, correct_answer
