import prompt
attempts = 3


def brain_games(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.task)
    for _ in range(attempts):
        correct_answer, number = game.calc_game()
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
