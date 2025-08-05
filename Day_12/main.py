from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check against the user actual answer
def check_answer(u_answer, a_answer, turns):
    if u_answer < a_answer:
        print("Too low.")
        return turns - 1
    elif u_answer > a_answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"you got it! The answer was {a_answer}.")
    
# make a function to set a difficulty level 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the answer is {answer}")  # For debugging purposes


    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        # let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns=turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!")


game()

