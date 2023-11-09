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
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        #position reset for next stage
        # chosen character for rogue and warrior
        self.playerResetR_X = WIDTH / 2 - 150
        self.playerResetR_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard
        self.playerResetW_X = WIDTH / 2 - 200
        self.playerResetW_Y = HEIGHT - HEIGHT / 3 - 100

        #make change later fighter
        self.enemy = Enemy(self.map)

        #game variable
        self.current_fighter = 1
        self.total_fighter = len(self.enemy.enemy_list)
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.battle_over = 0
        self.action_count = 3
        self.enemy_alive = len(self.enemy.enemy_list)



    def Enter(self, params):
        #make change
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Warrior":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Wizard":
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30,
                                          self.player.hp, self.player.max_hp)
        self.battle_menu = BattleMenu(self.player.action_list)
        pass

    def update(self, dt, events):
        #make change

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #select enemies to hit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.enemy.selected_enemy_index == 2:
                        self.enemy.selected_enemy_index = 1
                    else:
                        pass
                elif event.key == pygame.K_RIGHT:
                    if self.enemy.selected_enemy_index == 1:
                        self.enemy.selected_enemy_index = 2
                    else:
                        pass
                        
                #test attack key(w)
                if event.key == pygame.K_w:
                    self.attack = True
                    if self.player.alive == True:
                        if self.current_fighter == 1:
                            self.action_cooldown += 1
                            print(self.action_cooldown)
                            if self.attack == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                if self.action_count > 1:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.action_count -= 1
                                    self.action_cooldown = 0
                                else:
                                    self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                    self.action_count -= 1
                                    self.current_fighter += 1
                                    self.action_cooldown = 0
                            else:
                                pass


                    # self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                    else:
                        self.battle_over = -1
           
                
                #test player hurt
                # if event.key == pygame.K_r:
                #     for index, enemy in enumerate(self.enemy.enemy_list):
                #         print("pass loop")
                #         if self.current_fighter == 2 + index:
                #             print("pass check current fighter")
                #             if enemy.alive == True:
                #                 print("pass check enemy alive")
                #                 self.action_cooldown += 90
                #                 print(self.action_cooldown)
                #                 if self.action_cooldown >= self.action_wait_time:
                #                     print("pass check action coodown")
                #                     enemy.attack(self.player)
                #                     self.current_fighter += 1
                #                     self.action_cooldown = 0
                #             else:
                #                 self.current_fighter += 1 

                # test skill key(e)
                if event.key == pygame.K_e:
                    self.player.skill()

                if event.key == pygame.K_RETURN:
                    # update player position
                    if self.player.Class == "Rogue":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_X
                    elif self.player.Class == "Warrior":
                        self.player.X = self.playerResetR_X
                        self.player.Y = self.playerResetR_Y
                    elif self.player.Class == "Wizard":
                        self.player.X = self.playerResetW_X
                        self.player.Y = self.playerResetW_Y

                    #sound
                    #reset if want player to have full hp
                    #self.player.reset()
                    self.enemy.enemy_list[0].reset()
                    self.confirm_sound.play()
                    gSounds['music'].stop()
                    gSounds['late-hours'].play(-1)
                    gSounds['campfire_fireplace'].play(-1)

                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

        for index, enemy in enumerate(self.enemy.enemy_list):
            print("pass loop")
            if self.current_fighter == 2 + index:
                print("pass check current fighter")
                if enemy.alive == True:
                    print("pass check enemy alive")
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        print("pass check action coodown")
                        enemy.attack(self.player)
                        self.current_fighter += 1
                        self.action_cooldown = 0
                else:
                    self.current_fighter += 1            
    

    def is_enemy_alive(self):
        for enemy in self.enemy.enemy_list:
            if enemy.alive == True:
                self.enemy_alive -= 1
        if self.enemy_alive == 0:
            self.game_over = 1

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
