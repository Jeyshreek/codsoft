import random

def get_user_choice():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice (rock, paper, or scissors): ")
    return input().lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
