import prompt
ATTEMPTS = 3


def launch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for _ in range(ATTEMPTS):
        number, correct_answer = game.generator()
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
