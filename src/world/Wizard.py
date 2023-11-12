import pygame
from .Character import Character
from src.Dependencies import gWizardBattle_image_list
from src.world.DamageText import DamageText
from pygame.sprite import Group
import random
import math


class Wizard(Character):
    def __init__(self, x, y):
        super().__init__(gWizardBattle_image_list, max_hp = 80, strength = 13)
        self.X = x
        self.Y = y+15
        self.Class = "Wizard"
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
        self.rect.center = (self.X, self.Y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength * 0.9))
        for enemy in target:
            # run enemy hurt animation
            enemy.hurt(damage)
            #set variables to attack animation
            if enemy.hp < 1:
                enemy.hp = 0
                enemy.alive = False
                enemy.death()
            self.damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(damage), (255, 255, 255))
            self.damage_text_group.add(self.damage_text)
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    
    def skill_1(self, target):
        self.rect.center = (self.X, self.Y)
        # deal damage to enemy
        damage = int(math.ceil(self.strength * 1.7))
        for enemy in target:
            # run enemy hurt animation
            enemy.hurt(damage)
            #set variables to attack animation
            if enemy.hp < 1:
                enemy.hp = 0
                enemy.alive = False
                enemy.death()
            self.damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(damage), (255, 255, 255))
            self.damage_text_group.add(self.damage_text)
        self.action = 5
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def skill_2(self): 
        if self.skill_cooldown_2 == 0:
            self.original_str = self.strength
            self.strength = int(math.ceil(self.strength * 1.3))
            hp_down = int(math.ceil(10 + 0.15*self.max_hp))
            if self.hp < hp_down:
                self.hp = 1
            else:
                self.hp -= hp_down
            self.skill_cooldown_2 = 4
            self.action = 1
            self.frame_index = 6
            self.update_time = pygame.time.get_ticks()
            

    def hurt(self, damage):
        super().hurt(damage)
    
    def death(self):
        super().death()

    def reset(self):
        super().reset()
        self.action_count = 3
    
    def draw(self):
        super().draw()
    