logo = '''       
 _____ _   _ _____ _____ _____   _____ _   _  _____   _   _ _   ____  _________ ___________ 
|  __ \ | | |  ___/  ___/  ___| |_   _| | | ||  ___| | \ | | | | |  \/  || ___ \  ___| ___ \
| |  \/ | | | |__ \ `--.\ `--.    | | | |_| || |__   |  \| | | | | .  . || |_/ / |__ | |_/ /
| | __| | | |  __| `--. \`--. \   | | |  _  ||  __|  | . ` | | | | |\/| || ___ \  __||    / 
| |_\ \ |_| | |___/\__/ /\__/ /   | | | | | || |___  | |\  | |_| | |  | || |_/ / |___| |\ \ 
 \____/\___/\____/\____/\____/    \_/ \_| |_/\____/  \_| \_/\___/\_|  |_/\____/\____/\_| \_|
                                                                                            
                                                                                            
'''
import random
print(logo)
print("Welcome to the GUESS THE NUMBER game!")
number_of_choice = random.choice(range(0, 101))
game_style = input("Choose the game style. Type 'hard' or 'easy' to start: ")
user_guess = int(input("Guess a number between (1-100): "))
if game_style.lower() == "hard":
    player_guess_count = 5
    for attempt in range(1, 6):
        player_guess_count -= 1
        if player_guess_count == 0:
            print(f"You failed to guess the number within the allowed attempts! The answer was {number_of_choice}. ")
        elif user_guess > number_of_choice:
            user_guess = int(input(f"Your guess is too high! You have {player_guess_count} guesses left. Take another guess: "))
            continue
        elif user_guess < number_of_choice:
            user_guess = int(input(f"Your guess is too low! You have {player_guess_count} guesses left. Take another guess: "))
            continue
        elif user_guess == number_of_choice:
            print(f"Congratulations!!! You guessed the number correctly! You still had {player_guess_count} guesses left.")
            break
        else:
            print("You typed an invalid thing!!")
            break
elif game_style.lower() == "easy":
    player_guess_count = 10
    for attempt in range(1, 11):
        player_guess_count -= 1
        if player_guess_count == 0:
            print(f"You failed to guess the number within the allowed attempts! The answer was {number_of_choice}. ")
        elif user_guess > number_of_choice:
            user_guess = int(input(f"Your guess is too high! You have {player_guess_count} guesses left. Take another guess: "))
            continue
        elif user_guess < number_of_choice:
            user_guess = int(input(f"Your guess is too low! You have {player_guess_count} guesses left. Take another guess: "))
            continue
        elif user_guess == number_of_choice:
            print(f"Congratulations!!! You guessed the number correctly! You still had {player_guess_count} guesses left.")
            break
        else:
            print("You typed an invalid thing!!")
            break
else:
    print("You typed an invalid game style.")
input("Press enter to exit: ")