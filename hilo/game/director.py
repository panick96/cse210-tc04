from game.dealer import Dealer
from game.highscore import Highscore

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
        self.highscore = Highscore()

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
        self.dealer.draw_card()
        print(f"The card is {self.dealer.prev_card}")
        self.user_H_L_choice = input("Higher or Lower? [h/l] ")
        print(f"The next card was {self.dealer.current_card}")


    def do_updates(self):
        """
        This will adjust data based off of user's choices

        """
        if self.user_H_L_choice == self.dealer.determine_result():
            self.points += 100
        elif self.user_H_L_choice != self.dealer.determine_result():
            self.points -= 75
        else:
            self.points += 0

    def do_outputs(self):
        """
        Outputs the last bit of data, as well as some last minute proccessing
        """
        self.highscore.get_highscore()
        check_points = int(self.points)
        self.highscore.check_highscore(check_points)
        self.highscore.save_highscore
        if self.points <= 0:
            print('YOU LOSE')
            self.keep_playing == False
            quit()
        else:
            print(f'Points = {self.points}')
            self.get_choice = input("Keep Playing? [y/n] ")

            if self.get_choice == 'y':
                self.keep_playing == True
            elif self.get_choice == 'n':
                self.highscore.get_highscore()
                check_points = int(self.points)
                self.highscore.check_highscore(check_points)
                self.highscore.save_highscore()
                print(f'Your highscore was: {self.highscore.highscore}')
                self.keep_playing == False
                quit()
