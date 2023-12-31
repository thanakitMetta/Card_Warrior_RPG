import pygame
from src.world.items.BaseItem import BaseItem
from src.Dependencies import gItemGravity_image_list

class GravityItem(BaseItem):
    def __init__(self, x, y, player):
        super().__init__(gItemGravity_image_list, "Gravity Orb",
                         "Gravity is the primordial form magic",
                         "Said to increase wielder health")
        self.player = player
        self.X = x
        self.Y = y
        self.rect.center = (self.X, self.Y)

    def update(self):
        super().update()

    def idle(self):
        # set variables to idle animation
        super().idle()
        self.rect.center = (self.X, self.Y)

    def draw(self):
        super().draw()

    def action(self):
        self.player.max_hp += 30
        pass