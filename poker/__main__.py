from .classes.poker_classes import Card, Deck, Player, Game
import random

# def game(num_players=3):
#     # Game loop to deal with each game
#     game_number = 1
#     deck = Deck()
#     print("Starting game with {} players\n".format(num_players))
#     players = []
#     for i in range(num_players):
#         players.append(Player(i+1))
#         print(players[i].name, players[i].money)
    
#     print("You are player 1, you are the dealer for this round and you have £{}.".format(players[0].money))
#     next = input("Please press enter to begin the dealing, or press m to view your balance: ")
#     while next != '':
#         if next == 'm':
#             print("You have £{}.".format(players[0].money))
#         next = input("Please press enter to begin the dealing, or press m to view your balance: ")
    
#     play_round()
#     game_number += 1 # Change after game, also shuffle after each game


# def play_round():
#     print("Dealing round")
#     print(deck[0:10])
#     dealer = (game_number - 1) % num_players # Dealer number from 0,1,...
#     players[dealer].make_dealer()
#     for i in range(2*num_players):
#         dealt_card = deck.deal()
#         print("Card to deal is: {}".format(dealt_card))
#         players[(i+dealer+1)%num_players].receive(dealt_card)
#         print("Player {} received {}".format(players[(i+dealer+1)%num_players].name, players[(i+dealer+1)%num_players].cards))
#     print("Dealing hand...")



def main():
    # Main loop to play a game, and handle endgame
    Game()

    

if __name__ == '__main__':
    main()
