from random import randint
task = 'What number is missing in the progression?'


def games():
    step = randint(2, 7)
    start = randint(1, 50)
    stop = randint(100, 200)
    num_quantity = randint(5, 10)
    prog = [_ for _ in range(start, stop, step)][:num_quantity]
    index = randint(0, len(prog) - 1)
    correct_answer = prog[index]
    prog[index] = '..'
    number = ' '.join(map(str, prog))
    return number, str(correct_answer)
