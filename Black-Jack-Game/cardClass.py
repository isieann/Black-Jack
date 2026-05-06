import pygame

class Card:
    y = 380
    back = 'back.png'

    def __init__(self,c,s,v):
        self.card = c
        self.suit = s
        self.val = v
        self.file = 'na'
        self.x = 10
    
    def __str__(self):
        return f"{self.card} of {self.suit}"

    def cor(self,a):
        self.x = a
