#Have player pick rock, paper, or scissors
import random

#Keeping Score
player_score = 0
computer_score = 0


#GAME END PRINTS
draw = "DRAW!"
win = "YOU WIN!!"
lose = "YOU LOST!"

#List for computer to pick from
computer_list = ["rock", "paper", "scissors"]



while player_score != 3 and computer_score != 3:
    player_choice = input("Rock Paper or Scissors").lower().strip()
    #computer_choice = input("Rock Paper or Scissors").lower().strip()
    computer_choice = random.choice(computer_list)

    #Player wins
    if player_choice == "rock" and computer_choice == "scissors":
        player_score = player_score + 1
        print(player_score, "to", computer_score)
    if player_choice == "paper" and computer_choice == "rock":
        player_score = player_score + 1
        print(player_score, "to", computer_score)
    if player_choice == "scissors" and computer_choice == "paper":
        player_score = player_score + 1
        print(player_score, "to", computer_score)




    #Computer Wins
    if player_choice == "rock" and computer_choice == "paper":
        computer_score = computer_score + 1
        print (player_score, "to", computer_score)
    if player_choice == "paper" and computer_choice == "scissors":
        computer_score = computer_score + 1
        print (player_score, "to", computer_score)
    if player_choice == "scissors" and computer_choice == "rock":
        computer_score = computer_score + 1
        print(player_score, "to", computer_score)




    #Determines Draw
    if player_choice == "rock" and computer_choice == "rock":
        print(draw)
        print(player_score, "to", computer_score)

    elif player_choice == "paper" and computer_choice == "paper":
        print(draw)
        print(player_score, "to", computer_score)

    elif player_choice == "scissors" and computer_choice == "scissors":
        print(draw)
        print(player_score, "to", computer_score)


    #Win Conditions
    if player_score == 3:
        print(win)
    if computer_score == 3:
        print(lose)