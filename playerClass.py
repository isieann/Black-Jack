class Player:

    MAX = 21

    def __init__(self):
        self.handVal = 0
        self.hand = []
        self.gamesWon = 0

    def __str__(self):
        return f"{self.name}'s HAND VALUE is {self.handVal}".center(85)
    
    def check(self):
        if self.handVal >= self.MAX:
            return True
        else:
            return False
        

    def hit(self):
        pass
        
    def displayHand(self):
        pass

    def reset(self):
        self.handVal = 0
        self.hand = []

class Dealer(Player):

    def hit(self):
        if self.handVal <= 16:
            return True
        else:
            return False