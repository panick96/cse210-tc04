from game.deck import Deck


class Dealer():
    """
    This class of objects is for a dealer who draws the cards, keeps track
    of the previous card, and determines if the drawn card is hi or lo.

    Attributes:
        deck: instance of Deck class
        current_card: a random card drawn from the deck
        prev_card: the previous card, used to evaluate hi/lo
    """

    def __init__(self):
        """Class constructor. Defines instance attributes.

        Args:
            self (Dealer): An instance of the Dealer class.
        """
        self.deck = Deck()
        self.current_card = self.deck.draw_card()
        self.prev_card = 0

    def draw_card(self):
        """Gets a new card and retains the previous card.

        Args:
            self (Dealer): An instance of the Dealer class.
        """
        self.prev_card = self.current_card
        self.current_card = self.deck.draw_card()

    def determine_result(self):
        """ Determines if the drawn (current) card is higher or lower than
        the previous card.

        Args:
            self (Dealer): An instance of the Dealer class.
        Returns:
            str: if higher, returns 'hi'
                 if lower, returns 'lo'
                 if equal, returns 'equal'
        """
        if self.current_card > self.prev_card:
            result = 'h'
        elif self.current_card < self.prev_card:
            result = 'l'
        elif self.current_card:
            result = 'equal'
        return result
