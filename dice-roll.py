import os
import random

min = 1
max = 6

roll = input("Want to roll the dice, y/n?")
one = ["-----", "|   |", "| * |", "|   |", "-----"]
two = ["-----", "|*  |", "|   |", "|  *|", "-----"]
three = ["-----", "|*  |", "| * |", "|  *|", "-----"]
four = ["-----", "|* *|", "|   |", "|* *|", "-----"]
five = ["-----", "|* *|", "| * |", "|* *|", "-----"]
six = ["-----", "|* *|", "|* *|", "|* *|", "-----"] 

diceRoll = []

while roll == "y":
    i = 0
    while i < 6:
        num = random.randint(min, max)
        if num == 1:
            diceRoll.append(one)
        elif num == 2:
            diceRoll.append(two)
        elif num == 3:
            diceRoll.append(three)
        elif num == 4:
            diceRoll.append(four)
        elif num == 5:
            diceRoll.append(five)
        else:
            diceRoll.append(six)
        i += 1

    row = 0
    while row < 5:
        for die in diceRoll:
            print(die[row], end="\t")
        print("\r")
        row = row + 1
    
    roll = input("Want to roll the dice?")