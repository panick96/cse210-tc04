"""
Deck class that manages the cards
"""
import random
class Deck:
    

    def __init__(self) -> None:
        self.deck = []        
        self.card_choice = 0
        

    def create_deck (self):
        """
        args : instance of deck
        creates a deck and assigns it to self.deck
        """
        counter = 0

        for card in range(13):            
            counter += 1
            self.deck.append(counter)
    
    def draw_card(self):
        """
        args : instance of deck
        assigns card_choice to an integer
        """
        choice = random.choice(self.deck)
        index = choice - 1
        card = self.deck[index]
        self.card_choice = card
        del self.deck[index]
        return self.card_choice

        
            
"""
test = Deck()

test.create_deck()

print(test.deck)
test.draw_card()
print(test.card_choice)       
print(test.deck)
"""
