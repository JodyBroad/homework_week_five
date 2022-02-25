# rock, paper, scissors game

# three stages - 1 - get user input, convert it to Rock Paper Scissors
# 2 - generate computer action, convert it to Rock Paper Scissors
# 3 - compare the two and declare a winner

# we will need to generate random numbers later so:
import random

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

# prompt user to enter a value: R, P or S
player_1 = input("Please select your fighter: R = Rock, P = Paper, S = Scissors: ")
# print(player_1)

# need something here for if they enter something that isn't R P or S

# convert this input into Rock, Paper or Scissors

def convert_player_1(player_1):
    if player_1 == "R":
        player_1_action = "Rock"
    elif player_1 == "P":
        player_1_action = "Paper"
    elif player_1 == "S":
        player_1_action = "Scissors"
    return player_1_action


player_1_action = convert_player_1(player_1)

print("You chose: ", player_1_action)

# generate a random value between 0 and 2
player_2_action = actions[random.randint(0, 2)]
print("The computer chose: ", player_2_action)

# compare the user's choice against the computer's choice and then display a message as to if the user won, lost or drew
def who_wins(player_1_action, player_2_action):
    if player_1_action == player_2_action:
        print("Both players selected the same, it is a tie")
    elif player_1_action == "Rock":
        if player_2_action == "Scissors":
            print("Rock breaks scissors, so you are victorious!")
        else:
            print("Paper wraps rock, so you have been defeated")
    elif player_1_action == "Paper":
        if player_2_action == "Rock":
            print("Paper wraps rock, so you are victorious!")
        else:
            print("Scissors cut paper, so you have been defeated")
    elif player_1_action == "Scissors":
        if player_2_action == "Paper":
            print("Scissors cut paper, so you are victorious!")
        else:
            print("Rock breaks scissors, so you have been defeated")


who_wins(player_1_action, player_2_action)


# showcase what you have learned about conditional statements and create your own functions
