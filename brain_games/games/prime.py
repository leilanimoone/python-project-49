from random import randint
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
            break
        divisor += 1
    return True


def generator():
    number = randint(2, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer
