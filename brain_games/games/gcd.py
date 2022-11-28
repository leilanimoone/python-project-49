from random import randint
TASK = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    if num1 == num2:
        correct_answer = num1
    elif max(num1, num2) % min(num1, num2) == 0:
        correct_answer = min(num1, num2)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    return correct_answer


def generator():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    number = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return number, correct_answer
