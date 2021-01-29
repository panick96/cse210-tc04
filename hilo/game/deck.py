"""
Deck class that manages the cards
"""
import random
class Deck:
    

    def __init__(self) -> None:
        self.deck = []
        
        self.card_choice = 0
        

    def create_deck (self):
        counter = 0

        for card in range(10):            
            counter += 1
            self.deck.append(counter)
    
    def draw_card(self):
        choice = random.choice(self.deck)
        index = choice - 1
        card = self.deck[index]
        self.card_choice = card
        del self.deck[index]

        
            

test = Deck()
"""
test.create_deck()

print(test.deck)
test.draw_card()
print(test.card_choice)       
print(test.deck)
"""
