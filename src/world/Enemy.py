import pygame

class Enemy():
    def __init__(self, x, y, name, max_hp, damage):
        self.name = name
        self.position = (x,y)
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead, 4:skill, 5:skill
        self.update_time = pygame.time.get_ticks()
        self.add_animation_list(self.name)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def add_animation_list(self, name):
        for animation in name:
            self.animation_list.append(animation)

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 4:
                self.frame_index = len(self.animation_list[self.action]) - 1
            elif not self.alive:
                self.action = 4
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
            else:
                self.idle()
    
    def idle(self):
        # set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # self.hp -= damage
        # set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()




