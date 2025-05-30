import random
class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J","Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    #SUITS = clubs, diamonds, hearts and spades
    def __init__(self, rank, suit):
        """
        Creates a card by validating the rank and suit are in their respective lists
        :param rank: rank of the card
        :param suit:suit of the card
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Decorator that allows you to call the rank of a card as .rank instead of ._rank
        :return: rank
        """
        return self._rank

    @property
    def suit(self):
        """
        Decorator that allows you to call the suit of a card as .suit instead of ._suit
        :return: suit
        """
        return self._suit

    def __str__(self):
        """
        Magic method that defines the card as a string
        :return: string showing the rank and suit of a card
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Magic method that prints a string representation of the list of cards held within a container
        :return: list of cards
        """
        return self.__str__() #repr is the same as str

    def __eq__(self, other):
        """
        Checks if two cards are equal based on their rank
        :param other: second card
        :return: True if equal, False if different
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Checks if a card is less than another by looking at their rank
        :param other: second card
        :return: True if less, False if bigger
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        """
        Magic method that creates a standard deck of cards by looping through all combinations of rank and suits and appending each new object to a list
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Magic method that allows you to call the deck as .cards instead of ._cards
        :return: deck of cards
        """
        return self._cards

    def __str__(self):
        """
        Magic method that prints the deck as a string
        :return: deck of cards as a string
        """
        return str(self._cards)

    def shuffle(self):
        """
        Method to shuffle the deck of cards
        :return: shuffled deck
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Method to modify the deck by removing the first card from the list and returning  the top card from the deck
        :return: top card from the deck
        """
        return self.cards.pop(0)

if __name__=="__main__":
    c1 = Card("A","♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)