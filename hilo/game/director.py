from game.dealer import Dealer

class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        start_game: starts the game
        points: The total number of points earned.
        play_again: An instance of the class of objects known as Thrower.
        get_choice: See if they want to go high or low. 

    General Workflow:
        get_inputs
        do_updates
        do_outputs
    """
    def __init__(self):
        self.points = 0
        self.keep_playing = True
        self.user_H_L_choice = ""
        self.play_again = True
        self.get_choice = ""
        self.dealer = Dealer()

    def start_game(self):
        """
        Starts the game loop
        """

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """
        Prints and asks for the user input
        """
        print(f"The card is {self.dealer.previous_card}")
        self.user_H_L_choice = input("Higher or Lower? [h/l] ")
        print(f"The next card was {self.dealer.current_card")
        print(f'Your score is: {self.points}')
        self.get_choice = ("Keep Playing? [y/n] ")

    def do_updates(self):
        """
        This will adjust data based off of user's choices
        """

        






    

