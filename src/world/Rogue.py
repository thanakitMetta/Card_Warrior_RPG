import pygame
from .Character import Character
from src.Dependencies import gRogueBattle_image_list

class Rogue(Character):
    def __init__(self, x, y):
        super().__init__(gRogueBattle_image_list, max_hp = 100, strength = 3)
        self.X = x
        self.Y = y+15
        self.Class = "Rogue"
        self.action_list = ["W (Attack)", "Q (Evade)", "E (Slash)"]
        self.evade = False
        self.rect.center = (self.X, self.Y)
        self.action_count = 3
        self.skill_cooldown_1 = 0
        self.skill_cooldown_2 = 0
        self.acquired_joker = False
        self.turn_pass = 0 

    def update(self):
        super().update()


    def idle(self):
        super().idle()
        self.rect.center = (self.X, self.Y)

    def attack(self, target):
        self.rect.center = (self.X, self.Y)
        super().attack(target)

    
    def skill_1(self):
        self.rect.center = (self.X, self.Y)
        super().skill()
        if self.evade == False:
            self.evade = True
            self.skill_cooldown_1 = 3
        else:
            pass
    
    def skill_2(self, target):
        if self.skill_cooldown_2 == 0:
            self.rect.center = (self.X, self.Y)
            self.new_strength = self.strength * 1.5
            self.attack(target)
            self.skill_cooldown_2 = 2

    def hurt(self, damage):
        super().hurt(damage)
    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
        self.action_count = 3
    
    def draw(self):
        super().draw()
    