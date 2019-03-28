import random
def deck():
    Suits = ['spades', 'hearts','diamods', 'clubs']
    Suits2 = ['♠', '♥', '♦', '♣']
    Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    Deck = [(a, b) for a in Ranks for b in Suits2]
    return Deck

def main():

    my_deck = deck()
    random.shuffle(my_deck)
    print(my_deck)
main()
