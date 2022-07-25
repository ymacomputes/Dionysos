import random

min = 1
max = 6

roll = input("Want to roll the dice, y/n?")
one = "-----" + "\n" + "|   |" + "\n" + "| * |" + "\n" + "|   |" + "\n" + "-----"
two = "-----" + "\n" + "|*  |" + "\n" + "|   |" + "\n" + "|  *|" + "\n" + "-----"
three = "-----" + "\n" + "|*  |" + "\n" + "| * |" + "\n" + "|  *|" + "\n" + "-----"
four = "-----" + "\n" + "|* *|" + "\n" + "|   |" + "\n" + "|* *|" + "\n" + "-----"
five = "-----" + "\n" + "|* *|" + "\n" + "| * |" + "\n" + "|* *|" + "\n" + "-----"
six = "-----" + "\n" + "|* *|" + "\n" + "|* *|" + "\n" + "|* *|" + "\n" + "-----" 

while roll == "y":
    i = 0
    while i < 6:
        num = random.randint(min, max)
        if num == 1:
            print(one, end="")
        elif num == 2:
            print(two, end="")
        elif num == 3:
            print(three, end="")
        elif num == 4:
            print(four, end="")
        elif num == 5:
            print(five, end="")
        else:
            print(six, end="")
        i += 1
    print("-----")
    roll = input("Want to roll the dice?")