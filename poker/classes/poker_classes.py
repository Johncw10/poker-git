import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return "{}{}".format(self.rank,self.suit)
    

class Deck:
    def __init__(self):
        self.cards = self.instantiate()
        # for card in self.pack:
        #     print(card)
    
    def __getitem__(self, key):
        return self.cards[key]

    def instantiate(self, n_decks=1):
        deck = []
        for suit in {"C", "D", "H", "S"}:
            for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
                deck.append("{}{}".format(rank, suit))
        random.shuffle(deck)
        return deck
    
    def deal(self):
        return self.cards.pop(0)
    
    def burn(self):
        return self.cards.pop(0)


class Player:
    def __init__(self, name, money=100, dealer=False):
        self.cards = []
        self.money = money
        self.name = name
        self.dealer = dealer

    def deal(self):
        pass

    def receive(self, card):
        self.cards.append(card)
    
    def make_dealer(self):
        self.dealer = True


class Game:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.game_number = 1
        self.deck = Deck()
        print("Starting game with {} players\n".format(num_players))
        self.players = []
        for i in range(num_players):
            self.players.append(Player(i+1))
            print(self.players[i].name, self.players[i].money)
        
        print("You are player 1, you are the dealer for this round and you have £{}.".format(self.players[0].money))
        next = input("Please press enter to begin the dealing, or press m to view your balance: ")
        while next != '':
            if next == 'm':
                print("You have £{}.".format(self.players[0].money))
            next = input("Please press enter to begin the dealing, or press m to view your balance: ")
        
        self.play_round()
        self.game_number += 1 # Change after game, also shuffle after each game
        print("Exiting game.")
    
    def play_round(self):
        print("Dealing round")
        print(self.deck[0:10])
        dealer = (self.game_number - 1) % self.num_players # Dealer number from 0,1,...
        self.players[dealer].make_dealer()
        for i in range(2 * self.num_players):
            dealt_card = self.deck.deal()
            print("Card to deal is: {}".format(dealt_card))
            self.players[(i+dealer+1)%self.num_players].receive(dealt_card)
            print("Player {} received {}".format(self.players[(i+dealer+1)%self.num_players].name, self.players[(i+dealer+1)%self.num_players].cards))
        take_bets(dealer)

    def flop_bets(self, dealer):
        pass

    def take_bets(self, dealer):
        pass


