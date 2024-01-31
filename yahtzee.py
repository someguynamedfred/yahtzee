#stage one of my yahtzee game
import random
    
# check if there are enough elements and assign random numbers to the list of dice. This is essentially the start of turn. 
import random
length = False
test_list = []

while length == False:
    if len(test_list) < 5:
        i = random.randint(1,6)
        test_list.append(i)
    elif len(test_list) == 5:
        length = True

print(test_list)

#how to append a list of dice rolls that are randomly generated and it looks nice
import random

n = 5

dice_rolls=[]

while n > 0:
    y = random.randint(1,6)
    dice_rolls.append(y)
    n -= 1

dice_letters = ["A", "B", "C", "D", "E"]

dice_number = 0

print("Dice Rolls\n--------")
for n in dice_rolls:
    print(" " + str(dice_letters[dice_number]) + "  |  " + str(dice_rolls[dice_number]))
    dice_number +=1
    
#make a scoring system
#if the kept dice equal a certain list of integers, then a certain score is awarded

#large_straight is worth 40 points
#large_straight = [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]

#small_straight is worth 30 points
#small_straight = [1, 2, 3, 4] or [2, 3, 4, 5] or [3, 4, 5, 6]

#3 of a kind has three matching elements and it is worth sum of dice

#4 of a kind has four matching elements and it is worth sum of dice

#full house has three of a kind and two of a kind and it is worth 25 points

#chance equals total value of all dice

#yahtzee is 50 points for first success and then 100 for each after that
