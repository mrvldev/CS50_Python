import random

cards = ["jack", "queen", "king", "ace", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

random.shuffle(cards)
for card in cards:
    print(f"{card}")
         