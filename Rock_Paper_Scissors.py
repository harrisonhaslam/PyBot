player_wins = 0
computer_wins = 0

import random

# Loop

while player_wins < 2 and computer_wins < 2:

  print("Let's play rock, paper, scissors!")
  player_choice = input("Choose 'Rock', 'Paper', or 'Scissors':").lower()
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)

  print(f"Computer chose: {computer_choice} ")

  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"  
  elif (player_choice == computer_choice):
    winner = "Tie"
  elif  (computer_choice == "rock" and player_choice == "scissors") or (computer_choice == "scissors" and player_choice == "paper") or (computer_choice == "paper" and player_choice == "rock"):
    winner = "Computer"
  else:
    winner = "Nobody"
    print("Invalid Input: Please try again.")

  if (winner == "Player"):
    print("You won!")
    player_wins += 1
  elif (winner == "Computer"):
    print("Computer won!")
    computer_wins += 1
  elif (winner == "Nobody"): 
    print("loading new game...")
  else:
    print("It's a tie")

  print(f"CurrentScore: Player: {player_wins}, Computer: {computer_wins}")

# Results

if player_wins > computer_wins:
  print("Congrats! You win!")
else:
  print("You Lose! Computer won!")  

# Updated for incorrect inputs making it so computer wins













