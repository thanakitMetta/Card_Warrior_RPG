import pygame
from Enemy import Enemy

class Knight(Enemy):
    super().__init__(x, y, health = 50, damage = 10)
