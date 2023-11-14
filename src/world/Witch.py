import pygame
from .Character import Character
from src.constants import *
from src.Dependencies import *
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Witch(Character):
    def __init__(self, x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 - 20):
        super().__init__(name = gWitchBattle_image_list, max_hp = 1000, strength = 30)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.enemy_type = "Boss"
        self.is_skill2_use = False

    def update(self):
        super().update()

    def idle(self):
        if self.hp > 60:
            self.action = 0
        else:
            self.action = 6
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        super().death()

    def hurt(self, damage):
        super().hurt(damage)

    def skill_1(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        if self.double_damage == True:
            damage = int(damage*2)
            self.double_damage = False
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.hp += int(0.05*(self.max_hp - self.hp))
        rand = random.randint(1, 4)
        if rand == 1:
            self.evade = True
        elif rand == 2:
            self.block = True
        elif rand == 3:
            self.double_damage = True
        self.strength += 2
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def skill_2(self, target):
        self.rect.center = (self.x, self.y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength)*1.3)
        if self.double_damage == True:
            damage = int(damage*2)
            self.double_damage = False
        # run enemy hurt animation
        target.hurt(damage)
        #set variables to attack animation
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        self.damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255, 0, 0))
        self.damage_text_group.add(self.damage_text)
        self.hp += int(0.05*(self.max_hp - self.hp))
        rand = random.randint(1, 4)
        if rand == 1:
            self.evade = True
        elif rand == 2:
            self.block = True
        elif rand == 3:
            self.double_damage = True
        self.strength += 2
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
        screen.blit(self.image, self.rect)


