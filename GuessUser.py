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
    print(f'Your Guess Is Right {random_number} Congrats xD')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C) ??').lower()
        if feedback == 'h':
            print('Too high')
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed the number {guess}, correctly')

  
computer_guess(10)