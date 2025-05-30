from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        """
        Method that deals a five card hand
        :param deck: poker deck
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Decorator that allows you to call the deck as .cards instead of ._cards
        :return: deck of cards
        """
        return self._cards

    def __str__(self):
        """
        Magic method that prints the deck as a string
        :return: deck of cards as a string
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Method that checks if the hand is a flush or not
        :return: True if flush, False if otherwise
        """
        for card in self._cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Goes over each hand and returns the amount of matches
        :return: total number of matches
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Method that checks if the hand has a pair
        :return: True if there is one pair, False if there is no pair
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Method that checks if the hand has two pairs
        :return: True if there is two pairs, False if otherwise
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        Method that checks if the hand has three pairs
        :return: True if there is three pairs, False if otherwise
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Method that checks if the hand has six pairs
        :return: True if there is six pairs, False if otherwise
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Checks if hand is a full house, 8 matches
        :return: True if full house, False if otherwise
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Checks if a hand is straight by validating if there no matches and the difference between the highest and lowest card is 4.
        ...
        :return: True if straight, False if otherwise
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True


matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        #print(hand)
        matches += 1
       # break

print(f"The probability of straight is {100*matches/count}%")




