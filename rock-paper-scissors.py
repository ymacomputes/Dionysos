import random

move = input("What move do you want to play? ")

print("rock" + "\n" + "paper" + "\n" + "scissors" + "\n" + "SHOOT!" + "\n")

min = 1
max = 3
num = random.randint(min, max)

if num == 1:
    print("rock " + move)
    if move == "sissors":
        print("you lose!")
    elif move == "rock":
        print("draw")
    elif move == "paper":
        print("you win!")
elif num == 2:
    print("paper " + move)
    if move == "sissors":
        print("you lose!")
    elif move == "rock":
        print("you win!")
    elif move == "paper":
        print("draw")
elif num == 3:
    print("scissors " + move)
    if move == "sissors":
        print("draw")
    elif move == "rock":
        print("you lose!")
    elif move == "paper":
        print("you win!")
