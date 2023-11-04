from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

#make change
from src.world.Player import *
from src.world.HealthBar import HealthBar

class BattleState(BaseState):
    def __init__(self, state_machine):
        super(BattleState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))

        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)

        #make change later fighter
        self.player = Player(WIDTH / 2 - 96, HEIGHT - HEIGHT / 3 + 60, gRogueBattle_image_list, 30, 10)
        self.playerHealth = HealthBar(WIDTH / 2 - 96 - 50, HEIGHT - HEIGHT / 3 - 30, self.player.hp, self.player.max_hp)
        #make change later enemy
        self.player2 = Player(WIDTH / 2 - 96 + 400, HEIGHT - HEIGHT / 3 + 60, gKnightBattle_image_list, 30, 10)
        self.player2Health = (
            HealthBar(WIDTH / 2 - 96 - 50 + 400, HEIGHT - HEIGHT / 3 - 30, self.player2.hp, self.player2.max_hp))

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
                if event.key == pygame.K_LEFT:
                    if self.current_character == 1:
                        self.unavailable_sound.play()
                    else:
                        self.available_sound.play()
                        self.current_character -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.current_character == 1:
                        self.unavailable_sound.play()
                    else:
                        self.current_character += 1
                        self.available_sound.play()

                #test attack key(w)
                if event.key == pygame.K_w:
                    self.player.attack(self.player2)

                # test attack key(w)
                if event.key == pygame.K_e:
                    self.player.skill(self.player2)

                if event.key == pygame.K_RETURN:
                    #sound
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

        self.player2.draw()
        self.player2Health.draw(self.player2.hp)
        self.player2.update()


        #make change later
        # Update frame index for animation (for instance, every 5 frames)


    def Exit(self):
        pass
