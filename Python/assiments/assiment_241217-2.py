import random
import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ")
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")
            print("Please note the correct spelling.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "The computer wins!"

def play_game():
    user_wins = 0
    computer_wins = 0
    tie = 0
    
    while True:
        clear_console()
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chooses: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)

        print(result)

        if result == "You win!":
            user_wins += 1
        elif result == "The computer wins!":
            computer_wins += 1
        else:
            tie += 1

        print(f"Score: You {user_wins} - {computer_wins} Computer, Ties: {tie}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "no":
            print("Thanks for playing!")
            play_game()
        else:
            break

play_game()