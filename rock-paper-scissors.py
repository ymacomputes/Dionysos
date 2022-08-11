import random

move = input("rock" + "\n" + "paper" + "\n" + "scissors" + "\n" + "SHOOT!" + "\n" + "--> ")

min = 1
max = 3
num = random.randint(min, max)

if num == 1:
    print("rock ")
    if move == "scissors":
        print("you lose!")
    elif move == "rock":
        print("draw")
    elif move == "paper":
        print("you win!")
elif num == 2:
    print("paper ")
    if move == "scissors":
        print("you lose!")
    elif move == "rock":
        print("you win!")
    elif move == "paper":
        print("draw")
else:
    print("scissors ")
    if move == "scissors":
        print("draw")
    elif move == "rock":
        print("you lose!")
    elif move == "paper":
        print("you win!")
