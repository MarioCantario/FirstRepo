import random

choice = input("Play game? (yes/no): ")

if choice.lower() == "yes":
    player_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)
    if computer_choice == "rock" and player_choice == "scissors":
        print("You LOSTTTT")
    elif computer_choice == "rock" and player_choice == "paper":
        print("Paper eats da rock ya win")
    elif computer_choice == "rock" and player_choice == "rock":
        print("Rock vs rock, it's a tie!")
    elif computer_choice == "paper" and player_choice == "rock":
        print("Paper beats rock, you lose!")
    elif computer_choice == "paper" and player_choice == "scissors":
        print("ugh you win")
    elif computer_choice == "paper" and player_choice == "paper":
        print("Paper vs paper, it's a tie!")
    elif computer_choice == "scissors" and player_choice == "paper":
        print("Scissors cut paper, you lose!")
    elif computer_choice == "scissors" and player_choice == "rock":
        print("Rock bombs scissors, easy win")
    elif computer_choice == "scissors" and player_choice == "scissors":
        print("what the flip its a tie")

elif choice.lower() == "no":
    print("Alright bucko, u scared")
else:
    print("Bro it says yes/no")
