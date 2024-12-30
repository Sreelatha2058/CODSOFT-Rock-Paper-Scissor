import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\n--- Rock-Paper-Scissors Game ---")
    print("Scores -> You: {} | Computer: {}".format(user_score, computer_score))
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")
    player_choice = input("Your choice: ").lower()
    
    if player_choice == 'exit':
        print("\nFinal Scores -> You: {} | Computer: {}".format(user_score, computer_score))
        print("Thanks for playing!")
        break
    
    if player_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    # Display updated scores after each round
    print("Updated Scores -> You: {} | Computer: {}".format(user_score, computer_score))
