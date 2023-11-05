import pygame
from .Player import Player
from Dependencies import gRogueBattle_image_list

class Rogue(Player):
    def __init__(self, x, y):
        super().__init__(x, y, gRogueBattle_image_list, max_hp = 100, strength = 10)
        self.Class = "Rougue"
        self.evade = False

    def update(self):
        super().update()


    def idle(self):
        super().idle()

    def attack(self, target):
        super().attack(target)
    
    def skill(self, target):
        super().skill(target)
        if self.evade == False:
            self.evade = True
        else:
            pass
        while self.evade:
            pass

    def hurt(self, damage):
        super().hurt(damage)

    def reset(self):
        super().reset()
    
    def draw(self):
        super().draw()
    