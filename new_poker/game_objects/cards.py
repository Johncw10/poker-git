from dataclasses import dataclass
from enum import Enum
from typing import Literal
import random


RANKS = {
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
}
RANK_LONG_NAMES = {
    "A": "Ace",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
}
SUITS = {"C", "D", "H", "S"}
SUIT_LONG_NAMES = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}


@dataclass
class Rank:
    value: str

    def __post_init__(self):
        self.long_name = RANK_LONG_NAMES[self.value]

    def __repr__(self):
        return self.value


@dataclass
class Suit:
    suit: str

    def __post_init__(self):
        self.long_name = SUIT_LONG_NAMES[self.suit]

    def __repr__(self):
        return self.suit


@dataclass
class Card:
    rank: str
    suit: str

    def __repr__(self):
        """
        Returns short format of card, such as:
        '2H', 'KS'
        """
        short_format = f"{self.rank}{self.suit}"
        return short_format

    def long_name(self):
        """
        Returns long format of card, such as:
        'Two of Hearts', 'King of Spades'
        """
        long_format = f"{self.rank.long_name} of {self.suit.long_name}"
        return long_format


class Deck:
    def __init__(self):
        self.cards = self.create_deck_cards()

    def __post_init__(self):
        """
        Calculate
        """
        self.length = len(self.cards)

    def __str__(self):
        """
        Return all information on deck
        """
        deck_info_str = f"Deck with {self.length} cards"
        return deck_info_str

    def create_deck_cards(self):
        """
        Generate deck of
        """
        _cards = []
        for suit in SUITS:
            for rank in RANKS:
                _cards.append(Card(rank, suit))
