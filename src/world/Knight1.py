import pygame
from .Enemy import Enemy
from src.constants import *
from src.Dependencies import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Knight1(Enemy):
    def __init__(self):
        super().__init__(x = WIDTH / 2 - 96 + 400, y = HEIGHT - HEIGHT / 3 + 40, name=gKnightBattle_image_list, max_hp = 50, damage = 10)

    def update(self):
        super().update()

    def idle(self):
        # set variables to idle animation
        super().idle()

    def death(self):
        # set variables to death animation
        super().death()

    def hurt(self):
        # self.hp -= damage
        # set variables to hurt animation
       super().hurt()

    def reset(self):
        self.alive = True
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, True, False), self.rect)


