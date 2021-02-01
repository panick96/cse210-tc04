"""
Keeps track of highscore
"""
from os import read
class Highscore:
    """
    initializes the Highscore class
    """
    def __init__(self) -> None:
        self.highscore = '0'
        self.check = False
        
    """
    reads the highscore from the txt file and returns it

    args: self - instance of Highscore
    """    
    def get_highscore(self):
        with open('hilo/game/hs.txt') as highscore:
            score = highscore.read()
            self.highscore = int(score)
            return self.highscore
            


    """
    saves the highscore and overwrites the txt file

    args: self - instance of Highscore
    """
    
    def save_highscore(self):
        with open('hilo/game/hs.txt','w') as save:
            highscore = str(self.highscore)
            save.write(highscore)

    """
    checks the current score to see if it qualifies as highscore

    args: self - instance of Highscore
          points - (int) points of current game 
    """
    def check_highscore(self,points):
        if points > self.highscore:
            self.highscore = points
        else:
            self.highscore = self.highscore
        highscore = self.highscore
        return highscore

