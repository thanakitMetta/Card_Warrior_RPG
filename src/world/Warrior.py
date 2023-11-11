import pygame
from .Character import Character
from src.Dependencies import gWarriorBattle_image_list

class Warrior(Character):
    def __init__(self, x, y):
        super().__init__(gWarriorBattle_image_list, max_hp = 100, strength = 10)
        self.X = x
        self.Y = y+15
        self.Class = "Warrior"
        self.action_list = ["W (Attack)", "Q (______)", "E (_______)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)
        self.action_count = 3
        self.skill_cooldown_1 = 0
        self.skill_cooldown_2 = 0
        self.acquired_joker = False

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y+120)
        super().attack(target)

    
    def skill(self):
        self.rect.center = (self.X, self.Y)
        super().skill()
        if self.evade == False:
            self.evade = True
        else:
            pass

    def hurt(self, damage):
        super().hurt(damage)
    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
        self.action_count = 3
    
    def draw(self):
        super().draw()
    