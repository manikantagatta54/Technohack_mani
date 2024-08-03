import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice(player):
    user_choice = input(f"Player {player}, enter your choice (rock, paper, scissors) or type 'exit' to quit: ").lower()
    if user_choice == 'exit':
        return 'exit'
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Enter again (rock, paper, scissors) or type 'exit' to quit: ").lower()
        if user_choice == 'exit':
            return 'exit'
    return user_choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'paper' and choice2 == 'rock') or \
         (choice1 == 'scissors' and choice2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        mode = input("Choose mode: 1 for Player vs Computer, 2 for Player vs Player, 3 to Exit: ")
        
        if mode == '3':
            print("Exiting the game. Goodbye!")
            break
        
        if mode == '1':
            user_choice = get_user_choice("1")
            if user_choice == 'exit':
                print("Exiting the game. Goodbye!")
                break
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            print(determine_winner(user_choice, computer_choice))
        
        elif mode == '2':
            player1_choice = get_user_choice("1")
            if player1_choice == 'exit':
                print("Exiting the game. Goodbye!")
                break
            player2_choice = get_user_choice("2")
            if player2_choice == 'exit':
                print("Exiting the game. Goodbye!")
                break
            print(determine_winner(player1_choice, player2_choice))
        
        else:
            print("Invalid mode selected.")

play_game()
