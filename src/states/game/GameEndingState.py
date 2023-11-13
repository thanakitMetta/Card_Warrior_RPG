from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

# make change
from src.world.Character import *
from src.world.Knight1 import Knight1
from src.world.HealthBar import HealthBar
from src.world.Rogue import Rogue
from src.world.BattleMenu import BattleMenu
from src.world.GenerateEnemy import Enemy

# text generator
from src.text_generator import TextGenerator

class GameEndingState(BaseState):
    def __init__(self, state_machine):
        super(GameEndingState, self).__init__(state_machine)
        # map image
        self.bg_image = pygame.image.load("./graphics/backgroundFinal.jpg")


        # loading BG
        self.loading_bg_img = pygame.image.load("./graphics/loading_5.png")
        self.loading_bg_img = pygame.transform.scale(self.loading_bg_img, (WIDTH + 5, HEIGHT + 5))

        #sound
        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)

        #text generator
        self.opening_font = gFonts['zelda']
        self.opening_text = " ignorant"
        self.opening_text2 = " should"
        self.opening_text3 = " remain"
        self.generator = TextGenerator(self.opening_text, self.opening_font, 100, HEIGHT / 2 - 200, 0.1, (220,20,60))
        self.generator2 = TextGenerator(self.opening_text2, self.opening_font, 100, HEIGHT / 2 - 100, 0.1, (220, 20, 60))
        self.generator3 = TextGenerator(self.opening_text3, self.opening_font, 100, HEIGHT / 2, 0.1, (220, 20, 60))
        self.generator4 = TextGenerator(self.opening_text, self.opening_font, 100, HEIGHT / 2 + 100, 0.1, (220, 20, 60))

        # final boss map
        self.map = 36
        self.demon_slayed = True

    def Enter(self, params):
        # sounds
        self.music_selected = gSounds['battle5']
        self.music_selected.play(-1)
        # make change
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.player.Y += 80
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 100, HEIGHT - HEIGHT / 3 - 50,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Warrior":
            self.player.Y += 80
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 100, HEIGHT - HEIGHT / 3 - 50,
                                          self.player.hp, self.player.max_hp)
        elif self.player.Class == "Wizard":
            self.player.Y += 70
            self.player.X += 40
            self.playerHealth = HealthBar(WIDTH / 2 - 96 - 100, HEIGHT - HEIGHT / 3 - 50,
                                          self.player.hp, self.player.max_hp)
            # if self.player.Class == "Rogue":
            # self.player.X = self.playerResetR_X
            # self.player.Y = self.playerResetR_X
            # elif self.player.Class == "Warrior":
            # self.player.X = self.playerResetR_X
            # self.player.Y = self.playerResetR_Y
            # elif self.player.Class == "Wizard":
            # self.player.X = self.playerResetW_X
            # self.player.Y = self.playerResetW_Y


            self.player.is_use_skill2 = False
        self.battle_menu = BattleMenu(self.player.action_list)
        # make change later fighter
        self.total_step = self.player.step_count
        self.ATK_increase = int(math.ceil(self.player.strength * 0.05))
        self.HP_increase = int(math.ceil(self.player.max_hp * 0.05))


        #call enemy
        self.enemy = Enemy(self.map)

        # game variable
        self.current_fighter = 1
        self.total_fighter = 1 + len(self.enemy.enemy_list)
        self.action_cooldown = 0
        self.action_wait_time = 90
        self.attack = False
        self.skill_1 = False
        self.skill_2 = False
        self.battle_over = 0
        self.enemy_alive = len(self.enemy.enemy_list)
        self.loading = 0
        pass

    def update(self, dt, events):
        # make change
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.loading > 80:
                # select enemies to hit
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

                    # test attack key(q)
                    if event.key == pygame.K_q:
                        self.attack = True
                        if self.player.alive == True:
                            if self.current_fighter == 1:
                                self.action_cooldown += 1
                                print(f"Action cooldown = {self.action_cooldown}")
                                if self.attack == True and self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Wizard":
                                            self.player.attack(self.enemy.enemy_list)
                                        else:
                                            self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Wizard":
                                            self.player.attack(self.enemy.enemy_list)
                                        else:
                                            self.player.attack(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.battle_over = -1


                    # test skill key(w)
                    elif event.key == pygame.K_w:
                        self.skill_1 = True
                        if self.player.alive == True:
                            if self.current_fighter == 1:
                                self.action_cooldown += 1
                                print(f"Action cooldown = {self.action_cooldown}")
                                if self.skill_1 == True and self.player.skill_cooldown_1 == 0:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Rogue":
                                            self.player.skill_1()
                                        elif self.player.Class == "Warrior" or self.player.Class == "Wizard":
                                            if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                                self.player.skill_1(self.enemy.enemy_list)
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Rogue":
                                            self.player.skill_1()
                                        elif self.player.Class == "Warrior" or self.player.Class == "Wizard":
                                            if self.enemy.enemy_list[self.enemy.selected_enemy_index - 1].alive:
                                                self.player.skill_1(self.enemy.enemy_list)
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.battle_over = -1
                    # test skill key(e)
                    elif event.key == pygame.K_e:
                        self.skill_2 = True
                        if self.player.alive == True:
                            if self.current_fighter == 1:
                                self.action_cooldown += 1
                                print(f"Action cooldown = {self.action_cooldown}")
                                if self.skill_2 == True and self.enemy.enemy_list[
                                    self.enemy.selected_enemy_index - 1].alive and self.player.skill_cooldown_2 == 0:
                                    if self.player.action_count > 1:
                                        if self.player.Class == "Wizard":
                                            self.player.skill_2()
                                        else:
                                            self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.action_cooldown = 0
                                    else:
                                        if self.player.Class == "Wizard":
                                            self.player.skill_2()
                                        else:
                                            self.player.skill_2(self.enemy.enemy_list[self.enemy.selected_enemy_index - 1])
                                        self.player.action_count -= 1
                                        self.current_fighter += 1
                                        self.action_cooldown = 0
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.battle_over = -1

                    elif event.key == pygame.K_RETURN:
                        # update player position
                        if self.player.Class == "Wizard" and self.player.is_use_skill2 == True:
                            self.player.strength = self.player.original_str
                        self.player.strength += self.ATK_increase
                        self.player.max_hp += self.HP_increase
                        #if self.player.Class == "Rogue":
                            #self.player.X = self.playerResetR_X
                            #self.player.Y = self.playerResetR_X
                        #elif self.player.Class == "Warrior":
                            #self.player.X = self.playerResetR_X
                            #self.player.Y = self.playerResetR_Y
                        #elif self.player.Class == "Wizard":
                            #self.player.X = self.playerResetW_X
                            #self.player.Y = self.playerResetW_Y
                        print(self.player.max_hp)
                        # sound
                        for e in self.enemy.enemy_list:
                            e.reset()

                        self.confirm_sound.play()
                        self.loading = 0
                        self.player.reset_pos = True
                        self.player.action_count = 3
                        self.player.skill_cooldown_1 = 0
                        self.player.skill_cooldown_2 = 0
                        # stop music
                        self.music_selected.stop()
                        self.state_machine.Change('EndingCut', {
                            'chosen': self.player, 'demon_slayed': self.demon_slayed
                        })

        for index, enemy in enumerate(self.enemy.enemy_list):
            if self.current_fighter == 2 + index:
                if enemy.alive == True and self.player.alive == True:
                    self.action_cooldown += 1
                    if self.action_cooldown >= self.action_wait_time:
                        enemy.attack(self.player)
                        self.current_fighter += 1
                        self.action_cooldown = 0
                else:
                    self.current_fighter += 1
            else:
                if self.current_fighter > self.total_fighter:
                    self.current_fighter = 1
                    self.player.turn_count += 1

        if self.player.action_count == 0:
            self.player.action_count = 3
            if self.player.skill_cooldown_1 > 0:
                self.player.skill_cooldown_1 -= 1
            if self.player.skill_cooldown_2 > 0:
                self.player.skill_cooldown_2 -= 1

        if self.player.Class == "Wizard":
            if self.player.turn_count == 2 and self.player.is_use_skill2 == True:
                self.player.strength = self.player.original_str
            elif self.player.skill_cooldown_2 == 0:
                self.player.turn_count = 0

        self.is_enemy_alive()

    def is_enemy_alive(self):
        self.enemy_alive = len(self.enemy.enemy_list)
        self.action_cooldown += 1
        if self.action_cooldown >= self.action_wait_time:
            for enemy in self.enemy.enemy_list:
                if enemy.alive == False:
                    self.enemy_alive -= 1
            if self.enemy_alive == 0:
                self.battle_over = 1

    def render(self, screen):
        # make change
        #text generator
        if not self.generator.fully_displayed:
            self.generator.text_generation()
        if not self.generator2.fully_displayed:
            self.generator2.text_generation()
        if not self.generator3.fully_displayed:
            self.generator3.text_generation()
        if not self.generator4.fully_displayed:
            self.generator4.text_generation()

        screen.blit(self.bg_image, (0, 0))
        # fighter & health
        self.player.draw()
        self.playerHealth.draw(self.player.hp)
        self.player.update()

        self.enemy.render_enemy()
        self.enemy.draw_pointer_enemy()
        font = pygame.font.Font('./fonts/font.ttf', 30)
        # display battle menus
        self.battle_menu.display_fighting_menu()

        # display skill cooldown
        skill_1_cooldown = font.render(('CD: (' + str(self.player.skill_cooldown_1) + 'turn)'), True, (255, 255, 255))
        screen.blit(skill_1_cooldown, (210, 320))

        skill_2_cooldown = font.render(('CD: (' + str(self.player.skill_cooldown_2) + 'turn)'), True, (255, 255, 255))
        screen.blit(skill_2_cooldown, (210, 360))

        # display action count
        total_turn_text = font.render(('Action: ' + str(self.player.action_count)), True, (255, 255, 255))
        screen.blit(total_turn_text, (WIDTH - 170, HEIGHT - 70))

        # loading
        if self.loading > 70:
            self.player.reset_pos = False
            if self.loading > 80:
                print(f"loading = {self.loading}")
            else:
                self.loading+=1
        else:
            font = pygame.font.Font('./fonts/font.ttf', 28)
            text = font.render('Loading...', True, (255, 255, 255))
            screen.blit(self.loading_bg_img, (0, 0))
            screen.blit(text, (WIDTH - 170, HEIGHT - 70))
            self.loading += 1

        if self.battle_over == 1:
            screen.blit(self.bg_image, (0, 0))
            t_enter = gFonts['zelda'].render("Victory"
                                             , False, (175, 53, 42))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("The card grant you"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 40))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("%d ATK and %d HP" % (self.ATK_increase, self.HP_increase)
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 80))
            screen.blit(t_enter, rect)
            t_enter = self.small_font.render("Press 'Enter' to continue your journey"
                                             , False, (255, 255, 0))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 + 120))
            screen.blit(t_enter, rect)

        # make change later
        # Update frame index for animation (for instance, every 5 frames)

    def Exit(self):
        pass