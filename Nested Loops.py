# Nested Loops

'''
for i in range (1,6): # Outer loop
    for j in range (1,11): # Inner loop
        result = i * j
        print(f"{i} * {j} = {result}")
    print()
'''

'''
rows = 5

for i in range(rows): # PRINT THE ROWS
    for j in range(i+1): #PRINT THE STARS
        print("*", end = " ")
    print()
'''

#RANDOM

import random

cards = ["Diamonds", "Hearts", "Clubs", "Spades"]
print(f"Original Arrangement: {cards}")
random.shuffle(cards)
print(f"Shuffled Arrangement: {cards}:")
