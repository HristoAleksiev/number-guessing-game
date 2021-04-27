from artwork import logo
import random


def welcome_message():
    """
    Displays the logo art and welcomes the player to the Number Guessing Game.
    """
    print(logo)
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
    )


def generate_number():
    """
    Returns a random numbner to be guessed by the player (between 1 and 100)
    """
    number_to_guess = random.randint(1, 101)
    return number_to_guess


def check_guess(guess, number_to_guess):
    """
    Checks if the guess made is correct, lower or higer than the number, prints feedback to the player.
    """
    if guess == number_to_guess:
        print(f"You got it! The answer was {guess}.")
        return 1
    elif guess > number_to_guess:
        print(f"Too high.")
        return 0
    elif guess < number_to_guess:
        print(f"Too low.")
        return 0


def define_attempts_amount():
    """
    Prints and Returns the ammount of guesses the player will have (easy = 10 attempts, hard = 5 attempts)
    """
    attempts_at_guessing = 0

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_difficulty == "easy":
        attempts_at_guessing = 10
        print(f"You have chosen the 'easy' difficulty, you have {attempts_at_guessing} attempts to guess")
        return attempts_at_guessing
    elif game_difficulty == "hard":
        attempts_at_guessing = 5
        print(f"You have chosen the 'hard' difficulty, you have {attempts_at_guessing} attempts to guess")
        return attempts_at_guessing
    else:
        print("Invalid difficulty option selected!")

    attempts_at_guessing = define_attempts_amount()
    return attempts_at_guessing


def get_player_guess():
    """
    Asks the player to make try and guess the generated number. Retruns the guess as an integer.
    """
    guess = int(input("Make a guess: "))
    return guess


def display_attempts_remaining(attempts_remaining):
    """
    Prints remaining attempts to the player.
    """
    if attempts_remaining > 0:
        print(
            f"Guess again.\nYou have {attempts_remaining} attempts remaining to guess the number."
        )
    else:
        print("You've run out of guesses, you lose.")


# main games algorythm
def game():
    welcome_message()
    guessing_attempts = define_attempts_amount()
    number_to_guess = generate_number()

    while guessing_attempts != -1:
        player_guess = get_player_guess()
        is_number_guessed = check_guess(player_guess, number_to_guess)

        guessing_attempts -= 1

        if is_number_guessed:
            break

        display_attempts_remaining(guessing_attempts)

        if guessing_attempts == 0:
            break


game()
