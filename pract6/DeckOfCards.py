import itertools
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


deck = list(itertools.product(ranks, suits))
random.shuffle(deck)


for card in deck:
    card_rank, card_suit = card
    print(f"{card_rank} of {card_suit}")



# Output:
# 8 of Clubs
# 7 of Diamonds
# 4 of Diamonds
# Ace of Spades
# 6 of Clubs
# 4 of Spades
# 3 of Hearts
# 5 of Spades
# 10 of Hearts
# 6 of Spades
# Ace of Hearts
# 3 of Diamonds
# Queen of Clubs
# 7 of Hearts
# 2 of Hearts
# 4 of Hearts
# 7 of Clubs
# Queen of Spades
# Queen of Diamonds
# 9 of Diamonds
# Jack of Spades
# King of Spades
# King of Diamonds
# Jack of Diamonds
# King of Clubs
# 8 of Hearts
# 2 of Clubs
# Queen of Hearts
# 2 of Spades
# 10 of Spades
# Ace of Diamonds
# 5 of Clubs
# Ace of Clubs
# 2 of Diamonds
# 8 of Diamonds
# 4 of Clubs
# 7 of Spades
# 3 of Clubs
# 10 of Clubs
# 6 of Diamonds
# 6 of Hearts
# 8 of Spades
# 10 of Diamonds
# 3 of Spades
# Jack of Hearts
# 5 of Hearts
# 9 of Clubs
# Jack of Clubs
# 5 of Diamonds
# King of Hearts
# 9 of Hearts
# 9 of Spades
