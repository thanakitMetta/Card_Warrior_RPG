import pygame
from src.constants import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        # update with new health
        self.hp = hp
        # calculate health ratio
        ratio = self.hp / self.max_hp * 100
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 100, 20))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, ratio, 20))

        font  = pygame.font.Font('./fonts/font.ttf', 24)
        player_HP = font.render((f'HP: {self.hp}'), True, (0, 0, 0))
        screen.blit(player_HP, (self.x+5, self.y))