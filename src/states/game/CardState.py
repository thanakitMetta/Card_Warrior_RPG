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
        self.bg_image = pygame.image.load("./graphics/backgroundCozyTable.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))
        self.current_sprite_flame = 0
        self.flameList = flame_image_list
        #make change
        self.player_X = WIDTH / 2 - 96
        self.player_Y = HEIGHT - HEIGHT / 3 + 70
        #card
        self.flameCurrentFace = 0
        self.cardList = gCard_image_list
        random.shuffle(self.cardList)
        self.frame_index_flame = 0
        self.current_sprite_card = 0
        self.card_stop = False
        #sound
        self.confirm_sound = gSounds['burning_card']
        self.confirm_sound2 = gSounds['confirm']
        #text above witch
        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)

    def Enter(self, params):
        self.player = params['chosen']
        if self.player.Class == "Rogue":
            self.player.X = self.player_X
            self.player.Y = self.player_Y
        elif self.player.Class == "Warrior":
            self.player.X = self.player_X
            self.player.Y = self.player_Y
        elif self.player.Class == "Wizard":
            self.player.X = self.player_X
            self.player.Y = self.player_Y - 60
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
                    gSounds['burning_continue'].stop()
                    self.card_stop = True
                    print(RollDiceState.GetDice(RollDiceState))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN and self.card_stop:
                    # self.state_machine.Change('play')
                    self.card_stop = False
                    #music
                    self.confirm_sound2.play()
                    gSounds['music'].play(-1)
                    # shuffle
                    random.shuffle(self.cardList)
                    self.state_machine.Change('battle', {
                        'chosen': self.player
                    })

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        card_x1 = 0
        card_x2 = 0
        card_x3 = 0
        card_x4 = 0
        card_x5 = 0
        card_xOpen =0
        flame_x = 0
        
        if RollDiceState.GetDice(RollDiceState) == 1:
            card_x1 = 289
            card_x2 = 434
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 144
            flame_x = 90
        elif RollDiceState.GetDice(RollDiceState) == 2:
            card_x1 = 144
            card_x2 = 434
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 289
            flame_x = 235
        elif RollDiceState.GetDice(RollDiceState) == 3:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 579
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 434
            flame_x = 380
        elif RollDiceState.GetDice(RollDiceState) == 4:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 724
            card_x5 = 869
            card_xOpen = 579
            flame_x = 525
        elif RollDiceState.GetDice(RollDiceState) == 5:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 579
            card_x5 = 869
            card_xOpen = 724
            flame_x = 670
        elif RollDiceState.GetDice(RollDiceState) == 6:
            card_x1 = 144
            card_x2 = 289
            card_x3 = 434
            card_x4 = 579
            card_x5 = 724
            card_xOpen = 869
            flame_x = 815

        screen.blit(gCardBack_image_list[0],(card_x1,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x2,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x3,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x4,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_x5,HEIGHT-HEIGHT/2-200))
        screen.blit(gCardBack_image_list[0],(card_xOpen,HEIGHT-HEIGHT/2-200))

        if self.card_stop:
            screen.blit(self.cardList[RollDiceState.GetDice(RollDiceState)-1], (card_xOpen, HEIGHT - HEIGHT / 2 - 200))
        else:
            t_enter = self.small_font.render("Press 'down' to burn the card of thy fate", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            # text above witch
            if self.current_sprite_flame >= len(self.flameList):
                self.current_sprite_flame = 0

            if self.frame_index_flame % 8 == 0:  # Change 5 to control animation speed
                self.current_sprite_flame += 1  # Update frame index
                if self.current_sprite_flame >= len(self.flameList):
                    self.current_sprite_flame = 0  # Reset frame index when it reaches the end
            flame_img = pygame.transform.scale(self.flameList[self.current_sprite_flame], (300,300))
            self.frame_index_flame += 1
        # Display the current frame of the character image
        #flame_img = pygame.transform.scale(self.flameList[self.current_sprite_flame], (100, 100))
            screen.blit(flame_img, (flame_x, HEIGHT - HEIGHT / 2 - 300))
            t_enter = self.small_font.render("Press 'down' to burn the card of thy fate", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2 - 10, HEIGHT / 3 - 10))
            screen.blit(t_enter, rect)



        #card
    def Exit(self):
        pass