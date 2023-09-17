import random


def shuffle(deck):
    random.shuffle(deck)


deck = list(range(52))
shuffle(deck)
for i in range(52):
    print(deck[i], end=" ")
    if i % 13 == 12:
        print()


# Output:
# 37 4 9 32 14 25 27 21 26 18 12 41 50
# 38 22 23 15 33 8 44 1 17 24 45 6 7
# 48 49 36 46 10 16 34 19 3 28 40 51 13
# 29 43 47 5 11 20 39 35 42 31 0 30 2
