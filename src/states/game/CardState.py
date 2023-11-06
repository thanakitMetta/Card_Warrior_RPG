from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *
from src.states.game.RollDiceState import *
# make change
#card
import random

class CardState(BaseState):
    def __init__(self, state_machine):
        super(CardState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("./graphics/backgroundCozy.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))

        #make change
        self.frame_index_witch = 0
        self.current_sprite_witch = 0
        #card
        self.cardList = gCard_image_list
        random.shuffle(self.cardList)
        self.frame_index_card = 0
        self.current_sprite_card = 0
        self.card_stop = False
        #sound
        self.confirm_sound = gSounds['confirm']
        #text above witch
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)

    def Enter(self, params):
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #press to down stop card
                if event.key == pygame.K_DOWN and not self.card_stop:
                    self.confirm_sound.play()
                    self.card_stop = True
                    print(RollDiceState.GetDice(RollDiceState))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and self.card_stop:
                    # self.state_machine.Change('play')
                    self.card_stop = False
                    #music
                    self.confirm_sound.play()
                    gSounds['campfire_fireplace'].stop()
                    gSounds['late-hours'].stop()
                    gSounds['music'].play(-1)
                    # shuffle
                    random.shuffle(self.cardList)
                    self.state_machine.Change('battle')

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        # witch
        screen.blit(gCardBack_image_list[0],(144,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(289,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(434,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(579,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(724,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(869,HEIGHT-HEIGHT/2-200))
        if self.card_stop:
            if self.current_sprite_witch >= len(gWitch2_image_list):
                self.current_sprite_witch = 0

            if self.frame_index_witch % 10 == 0:  # Change 5 to control animation speed
                self.current_sprite_witch += 1  # Update frame index
                if self.current_sprite_witch >= len(gWitch2_image_list):
                    self.current_sprite_witch = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = gWitch2_image_list[self.current_sprite_witch]
            screen.blit(character_img, (WIDTH / 2 - 96 + 16, HEIGHT - HEIGHT / 2 + 15))

            self.frame_index_witch += 1
        else:
            if self.current_sprite_witch >= len(gWitch_image_list):
                self.current_sprite_witch = 0

            if self.frame_index_witch % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite_witch += 1  # Update frame index
                if self.current_sprite_witch >= len(gWitch_image_list):
                    self.current_sprite_witch = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = gWitch_image_list[self.current_sprite_witch]
            screen.blit(character_img, (WIDTH / 2 - 96, HEIGHT - HEIGHT / 2 + 15))

            self.frame_index_witch += 1

        #text generation
        font = pygame.font.Font(None, 36)
        text = "Oh...Great being... Please role this card to accept the guidance of fate"


        #card
    def Exit(self):
        pass