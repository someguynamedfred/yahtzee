#stage one of my yahtzee game
import random

#this is the basic dice roll
cont = input("Do you want to continue?")
if cont == "yes" or cont == "y":
    dice = random.randint(1,6)
    print(dice)
    
# check if there are enough elements
length = False
test_list = []

while length == False:
    if len(test_list) < 5:
        test_list.append(1)
    elif len(test_list) == 5:
        length = True

print(test_list)
    
#make a scoring system
#if the kept dice equal a certain list of integers, then a certain score is awarded

#large_straight is worth 40 points
large_straight = [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]

#small_straight is worth 30 points
small_straight = [1, 2, 3, 4] or [2, 3, 4, 5] or [3, 4, 5, 6]

#3 of a kind has three matching elements and it is worth sum of dice

#4 of a kind has four matching elements and it is worth sum of dice

#full house has three of a kind and two of a kind and it is worth 25 points

#chance equals total value of all dice

#yahtzee is 50 points for first success and then 100 for each after that

test_list = [1, 2, 3, 5]
print(len(test_list))
