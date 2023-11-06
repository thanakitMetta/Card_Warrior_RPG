from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

#make change
from src.world.Character import *
from src.world.Knight1 import Knight1
from src.world.HealthBar import HealthBar
from src.world.Rogue import Rogue
from src.world.BattleMenu import BattleMenu
from src.world.GenerateEnemy import Enemy

class BattleState(BaseState):
    def __init__(self, state_machine):
        super(BattleState, self).__init__(state_machine)
        self.map = 0
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.player_X = WIDTH / 2 - 96
        self.player_Y = HEIGHT - HEIGHT / 3 + 70
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)

        #make change later fighter
        self.player = Rogue(self.player_X, self.player_Y)
        self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30, self.player.hp, self.player.max_hp)
        #make change later enemy
        self.enemy = Enemy(self.map)
        #make battle menu
        self.battle_menu = BattleMenu(self.player.action_list)

        #current map

    def Enter(self, params):
        #make change
        pass

    def update(self, dt, events):
        #make change

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #make change
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.battle_menu.pointer_index = (self.battle_menu.pointer_index + 1) % len(self.player.action_list)
                elif event.key == pygame.K_UP:
                    self.battle_menu.pointer_index = (self.battle_menu.pointer_index - 1) % len(self.player.action_list)

                #test attack key(w)
                if event.key == pygame.K_w:
                    self.player.attack(self.enemy.Enemy1)
                    if self.enemy.Enemy1.hp <= 0:
                        self.enemy.Enemy1.death()
           
                
                #test player hurt
                if event.key == pygame.K_r:
                    self.enemy.Enemy1.attack(self.player)
                    if self.player.hp <= 0:
                        self.player.death()

                # test skill key(e)
                if event.key == pygame.K_e:
                    self.player.skill()

                if event.key == pygame.K_RETURN:
                    #sound
                    self.player.reset()
                    self.enemy.Enemy1.reset()
                    self.confirm_sound.play()
                    gSounds['music'].stop()
                    gSounds['late-hours'].play(-1)
                    gSounds['campfire_fireplace'].play(-1)

                    self.state_machine.Change('roll')


    def render(self, screen):
        #make change
        screen.blit(self.bg_image, (0, 0))
        #fighter & health
        self.player.draw()
        self.playerHealth.draw(self.player.hp)
        self.player.update()

        self.enemy.render_enemy()
        self.enemy.draw_pointer_enemy()

        #display battle menus
        self.battle_menu.display_fighting_menu()

        #make change later
        # Update frame index for animation (for instance, every 5 frames)


    def Exit(self):
        pass
