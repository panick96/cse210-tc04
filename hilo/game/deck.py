"""
Deck class that manages the cards
"""
import random
class Deck:
    

    def __init__(self) -> None:
        self.deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]        
        self.card_choice = 0
        

    def create_deck (self):
        """
        args : instance of deck
        creates a deck and assigns it to self.deck
        """
        counter = 0
        print('Shuffling Deck')
        for card in range(13):            
            counter += 1
            for i in range(4):
                self.deck.append(counter)
    
    def draw_card(self):
        """
        args : instance of deck
        assigns card_choice to an integer
        """
        choice = random.choice(self.deck)
        index = self.deck.index(choice)
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