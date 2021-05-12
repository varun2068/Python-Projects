import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a Number between 1 and {}:'.format(x)))
        if guess < random_number:
            print('Sorry, Guess again. Too Low')
        elif guess > random_number:
            print('Sorry, Guess again. Too High')
        else:
            print(f'Your Guess Is Right {random_number} Congrats <3')

guess(10)        
