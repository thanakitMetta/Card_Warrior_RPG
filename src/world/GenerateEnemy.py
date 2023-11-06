import pygame
from src.constants import *
from src.world.Knight1 import Knight1
from src.world.HealthBar import HealthBar

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Enemy():
    def __init__(self, map_number):
        self.selected_enemy_index = 0
        self.map_number = map_number
        self.generate_enemy()

    def generate_enemy(self):
        self.enemy_list = []
        if self.map_number == 0:
            #knight number 1
            self.Enemy1 = Knight1(x = WIDTH / 2 - 96 + 500)
            self.enemy_list.append("Enemy1")
            self.Enemy1Health = HealthBar(WIDTH / 2 - 96 - 50 + 500, HEIGHT - HEIGHT / 3 - 30, self.Enemy1.hp, self.Enemy1.max_hp)
            self.Enemy1.draw()
            self.Enemy1Health.draw(self.Enemy1.hp)
            self.Enemy1.update()
            #knight number 2
            self.Enemy2 = Knight1(x = WIDTH / 2 - 96 + 300)
            self.enemy_list.append("Enemy2")
            self.Enemy2Health = HealthBar(WIDTH / 2 - 96 - 50 + 300, HEIGHT - HEIGHT / 3 - 30, self.Enemy2.hp, self.Enemy2.max_hp)
            self.Enemy2.draw()
            self.Enemy2Health.draw(self.Enemy2.hp)
            self.Enemy2.update()
    
    def render_enemy(self):
        if self.map_number == 0:
            #enemy1
            self.Enemy1.draw()
            self.Enemy1Health.draw(self.Enemy1.hp)
            self.Enemy1.update()
            #enemy2
            self.Enemy2.draw()
            self.Enemy2Health.draw(self.Enemy2.hp)
            self.Enemy2.update()

    def draw_pointer_enemy(self):
        self.arrow_x = self.Enemy1.x
        self.arrow_y = self.Enemy1.y + 120
        pygame.draw.polygon(screen, (255, 0, 0), [(self.arrow_x, self.arrow_y), (self.arrow_x + 10, self.arrow_y + 20), (self.arrow_x - 10, self.arrow_y + 20)]) 