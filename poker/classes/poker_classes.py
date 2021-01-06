import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return "{}{}".format(self.rank,self.suit)

class Deck:
    def __init__(self):
        self.pack = self.instantiate()
        for card in self.pack:
            print(card)

    def instantiate(self, n_decks=1):
        deck = []
        for suit in {"C", "D", "H", "S"}:
            for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
                deck.append("{}{}".format(rank, suit))
        # random.shuffle(deck)
        return deck