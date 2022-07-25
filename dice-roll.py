import random

print("""
  /-_-\\                 ____      _        _          _                              _                /-_-\\
 /  /  \\               |  _ \ ___| |_ __ _| |___     / \   _ __ ___  _   _ _ __   __| |              /  /  \\ 
/  /    \\              | |_) / _ \ __/ _` | / __|   / _ \ | '__/ _ \| | | | '_ \ / _` |             /  /    \\
\  \    /              |  __/  __/ || (_| | \__ \  / ___ \| | | (_) | |_| | | | | (_| |             \  \    /
 \__\__/               |_|   \___|\__\__,_|_|___/ /_/   \_\_|  \___/ \__,_|_| |_|\__,_|              \__\__/ 
    \\\\                                                                                                  \\\\
    -\\\\    ____                    _____ _            ____                                              -\\\\    ____
      \\\\  /   /                   |_   _| |__   ___  |  _ \ ___  ___  ___                                 \\\\  /   /
____   \\\\/___/                      | | | '_ \ / _ \ | |_) / _ \/ __|/ _ \\                          ____   \\\\/___/
\   \ -//                           | | | | | |  __/ |  _ < (_) \__ \  __/                          \   \ -//
 \___\//-                           |_| |_| |_|\___| |_| \_\___/|___/\___|                           \___\//-
    -//                                                                                                 -//
     \\\\                                          RULES:                                                  \\\\
     //                        1. The name of the game is petals around the rose.                        //
    //-                        2. Rule 1 is your only hint.                                             //-
  -//                          3. You have 3 guesses per roll.                                        -//
  //                           4. Do not share the secert.                                            //
""")

min = 1
max = 6

one = ["-----", "|   |", "| * |", "|   |", "-----"]
two = ["-----", "|*  |", "|   |", "|  *|", "-----"]
three = ["-----", "|*  |", "| * |", "|  *|", "-----"]
four = ["-----", "|* *|", "|   |", "|* *|", "-----"]
five = ["-----", "|* *|", "| * |", "|* *|", "-----"]
six = ["-----", "|* *|", "|* *|", "|* *|", "-----"] 

roll = input("Want to roll the dice, y/n? ")

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
            print("\t" + die[row], end="\t")
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