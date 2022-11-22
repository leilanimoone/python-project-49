from random import randint
task = 'Find the greatest common divisor of given numbers.'


def games():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    number = f'{num1} {num2}'
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
    return number, str(correct_answer)
