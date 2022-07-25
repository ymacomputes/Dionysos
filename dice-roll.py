import os
import random

min = 1
max = 6

roll = input("Want to roll the dice, y/n? ")
one = ["-----", "|   |", "| * |", "|   |", "-----"]
two = ["-----", "|*  |", "|   |", "|  *|", "-----"]
three = ["-----", "|*  |", "| * |", "|  *|", "-----"]
four = ["-----", "|* *|", "|   |", "|* *|", "-----"]
five = ["-----", "|* *|", "| * |", "|* *|", "-----"]
six = ["-----", "|* *|", "|* *|", "|* *|", "-----"] 

while roll == "y":
    diceRoll = []
    petalNum = 0
    i = 0
    while i < 6:
        num = random.randint(min, max)
        if num == 1:
            diceRoll.append(one)
        elif num == 2:
            diceRoll.append(two)
        elif num == 3:
            diceRoll.append(three)
            petalNum += 2
        elif num == 4:
            diceRoll.append(four)
        elif num == 5:
            diceRoll.append(five)
            petalNum += 4
        else:
            diceRoll.append(six)
        i += 1

    row = 0
    while row < 5:
        for die in diceRoll:
            print(die[row], end="\t")
        print("\r")
        row = row + 1

    petals = input("How many petals are there? ")
    for a in range(2):
        if int(petals) == petalNum:
            print("Congrats! You are correct.")
            break
        else:
            petals = input("Try again. ")
    
    print("There are " + str(petalNum) + " petals around the rose. ")
    roll = input("Want to roll again? ")