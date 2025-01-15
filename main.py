from tkinter.constants import CURRENT

import game_data
import random
import art

First_item = random.choice(game_data.data)
Second_item = random.choice(game_data.data)
if First_item == Second_item:
   Second_item = random.choice(game_data.data)
Total_Score = 0


def right_wrong(First_item, Second_item, Guess):
    global Total_Score
    A =  First_item['follower_count']
    B = Second_item['follower_count']
    Higher = max(A,B)
    print(Higher)
    if Guess == Higher:
        Current_Score = Total_Score +1
        Total_Score = Current_Score
        print(f'You are right !! Current score: {Total_Score}')
        right_repeat(First_item, Second_item)
    else:
        print(f'Sorry, that\'s wrong. Final Score: {Total_Score}')

def right_repeat(a,b):
    First_item = b
    Second_item = random.choice(game_data.data)

    if First_item == Second_item:
        Second_item = random.choice(game_data.data)
    print(First_item['follower_count'], Second_item['follower_count'])
    name = First_item['name']
    profession = First_item['description']
    place = First_item['country']
    print(art.logo)
    print(f'Cpmpare A: {name}, a {profession} from {place}')
    print(art.vs)
    name2 = Second_item['name']
    profession2 = Second_item['description']
    place2 = Second_item['country']
    Higher = max((First_item['follower_count']), (Second_item['follower_count']))
    print(f'Cpmpare B: {name2}, a {profession2} from {place2}')
    Guess = input('Who has more followers ? Type A or B: ')
    if Guess == 'A':
        Guess = First_item['follower_count']
    else:
        Guess = Second_item['follower_count']

    right_wrong(First_item, Second_item,Guess)


def game():
    print(First_item['follower_count'], Second_item['follower_count'])

    name = First_item['name']
    profession = First_item['description']
    place = First_item['country']
    print(art.logo)
    print(f'Cpmpare A: {name}, a {profession} from {place}')
    print(art.vs)
    name2 = Second_item['name']
    profession2 = Second_item['description']
    place2 = Second_item['country']
    Higher = max((First_item['follower_count']), (Second_item['follower_count']))
    print(f'Cpmpare B: {name2}, a {profession2} from {place2}')
    Guess = input('Who has more followers ? Type A or B: ')
    if Guess == 'A':
        Guess = First_item['follower_count']
    else:
        Guess = Second_item['follower_count']

    print(Guess)
    right_wrong(First_item, Second_item,Guess)
    #while Current_Score > Previous_Score:
        #right_repeat()



game()

