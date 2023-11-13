import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class KingOfDiamond(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 350, y = HEIGHT - HEIGHT / 3 + 40):
        super().__init__(name = gHashashinBattle_image_list, max_hp = 120, strength = 18)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Boss"

    def update(self):
        super().update()

    def idle(self):
        super().idle()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)
        self.hp -= damage
    
    def skill_1(self, target):
        self.rect.center = (self.X, self.Y)
        # deal damage to enemy
        self.strength += 5
        damage = int(math.ceil(self.strength)*1.3)
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 255, 255))
        self.damage_text_group.add(self.damage_text)
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def skill_2(self, target):
        self.rect.center = (self.X, self.Y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 255, 255))
        self.damage_text_group.add(self.damage_text)
        self.hp += 20
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    
    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, True, False), self.rect)


