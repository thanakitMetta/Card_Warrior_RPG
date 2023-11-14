from src.states.BaseState import BaseState
import pygame, sys

from src.constants import *
from src.Dependencies import *

#make change
#chosen character
from src.world.Rogue import Rogue
from src.world.Warrior import Warrior
from src.world.Wizard import Wizard

#text generator
from src.text_generator import TextGenerator

class CharacterSelectState(BaseState):
    def __init__(self, state_machine):

        super(CharacterSelectState, self).__init__(state_machine)
        self.bg_image = pygame.image.load("./graphics/background.png")
        self.bg_image = pygame.transform.scale(
            self.bg_image, (WIDTH + 5, HEIGHT + 5))

        # make change
        self.bg_image_winter = pygame.image.load("./graphics/backgroundWinter.png")
        self.bg_image_winter = pygame.transform.scale(
            self.bg_image_winter, (WIDTH + 5, HEIGHT + 5))

        self.bg_image_library = pygame.image.load("./graphics/backgroundLibraryDark.png")
        self.bg_image_library = pygame.transform.scale(
            self.bg_image_library, (WIDTH + 5, HEIGHT + 5))
        # change end

        self.current_character = 0

        self.unavailable_sound = gSounds['no-select']
        self.available_sound = gSounds['select']
        self.confirm_sound = gSounds['confirm']
        self.return_to_main_sound = gSounds['wall_hit']

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)

        #text generator
        font = pygame.font.Font('./fonts/font.ttf', 20)
        text = " I am Green Witch, and I request you, great being. The land is in chaos..."
        self.generator = TextGenerator(text, font, 50, HEIGHT / 2 - 80, 0.1, (255, 255, 255))
        text1 = " The sacred cards are scattered throughout the land. They exist to protect this land..."
        self.generator1 = TextGenerator(text1, font, 50, HEIGHT / 2 - 40, 0.1, (255, 255, 255))
        text2 = " They must not fall to the hand of wrong. Collect them for me, and I will protect them from other"
        self.generator2 = TextGenerator(text2, font, 50, HEIGHT / 2, 0.1, (255, 255, 255))
        text3 = " Would you accept my offer, great being?..."
        self.generator3 = TextGenerator(text3, font, 50, HEIGHT / 2 + 40, 0.1, (255, 255, 255))
        text4 = " Excellent. I knew you would accept my request. Let me take you the Library..."
        self.generator4 = TextGenerator(text4, font, 50, HEIGHT / 2 + 80, 0.1, (255, 255, 255))

        #turnoff skip
        self.generator.skip_able = True
        self.generator1.skip_able = True
        self.generator2.skip_able = True
        self.generator3.skip_able = True
        self.generator4.skip_able = True

        #make change later
        self.clock = pygame.time.Clock()
        self.frame_index = 0
        self.current_sprite = 0
        # Starting animation direction
        # Start with the first frame

        #CHARACTER
        self.player = 0
        # chosen character for rogue
        self.player_X = WIDTH / 2 - 150
        self.player_Y = HEIGHT - HEIGHT / 3 - 20
        # for wizard and warrior
        self.playerW_X = WIDTH / 2 - 200
        self.playerW_Y = HEIGHT - HEIGHT / 3 - 40

    def Enter(self, params):
        #make change
        pass

    def update(self, dt, events):
        #make change

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.current_character == 0:
                        self.unavailable_sound.play()
                    else:
                        self.available_sound.play()
                        self.current_character -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.current_character == 2:
                        self.unavailable_sound.play()
                    else:
                        self.current_character += 1
                        self.available_sound.play()

                if event.key == pygame.K_RETURN:
                    #sound
                    self.confirm_sound.play()
                    gSounds['music'].stop()
                    #character change
                    if self.current_character == 0:
                        self.player = Rogue(self.player_X, self.player_Y)
                    elif self.current_character == 1:
                        self.player = Warrior(self.player_X, self.player_Y)
                    elif self.current_character == 2:
                        self.player = Wizard(self.playerW_X, self.playerW_Y)

                    self.state_machine.Change('roll', {
                        'chosen': self.player
                    })

    def render(self, screen):
        #text generator
        if not self.generator.fully_displayed:
            self.generator.text_generation()
        if not self.generator1.fully_displayed:
            self.generator1.text_generation()
        if not self.generator2.fully_displayed:
            self.generator2.text_generation()
        if not self.generator3.fully_displayed:
            self.generator3.text_generation()
        if not self.generator4.fully_displayed:
            self.generator4.text_generation()


        if self.current_character == 0:
            screen.blit(self.bg_image, (0, 0))
        elif self.current_character == 1:
            screen.blit(self.bg_image_winter, (0, 0))
        elif self.current_character == 2:
            screen.blit(self.bg_image_library, (0, 0))

        t_instruct = self.medium_font.render("Select your character (left right)", False, (255, 255, 255))
        rect = t_instruct.get_rect(center=(WIDTH / 2, HEIGHT / 4))
        screen.blit(t_instruct, rect)

        #make change later
        # Update frame index for animation (for instance, every 5 frames)
        if self.current_character == 0:
            t_enter = self.small_font.render("Rogue", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2, HEIGHT / 3))
            screen.blit(t_enter, rect)

            #skill
            t_enter2 = self.small_font.render("Q Attack, W Evade 1 attack, E Deal critical damage", False, (255, 255, 255))
            rect2 = t_enter2.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
            screen.blit(t_enter2, rect2)

            if self.current_sprite >= len(gRogue_image_list):
                self.current_sprite = 0

            if self.frame_index % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite += 1  # Update frame index
                if self.current_sprite >= len(gRogue_image_list):
                    self.current_sprite = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = gRogue_image_list[self.current_sprite]
            rect = character_img.get_rect(midtop=(WIDTH / 2 - 96, HEIGHT - HEIGHT / 3))
            screen.blit(character_img, (WIDTH / 2 - 96, HEIGHT - HEIGHT / 3 + 15))

            self.frame_index += 1

        elif self.current_character == 1:
            t_enter = self.small_font.render("Warrior", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2, HEIGHT / 3))
            screen.blit(t_enter, rect)

            # skill
            t_enter2 = self.small_font.render("Q Attack, W Deal area damage and reduce damage taken, E Attack and heal",
                                              False,
                                              (255, 255, 255))
            rect2 = t_enter2.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
            screen.blit(t_enter2, rect2)

            if self.current_sprite >= len(gWarrior_image_list):
                self.current_sprite = 0

            if self.frame_index % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite += 1  # Update frame index
                if self.current_sprite >= len(gWarrior_image_list):
                    self.current_sprite = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = pygame.transform.scale(gWarrior_image_list[self.current_sprite], (346, 160))
            #character_img = gWarrior_image_list[self.current_sprite]
            rect = character_img.get_rect(midtop=(WIDTH / 2 - 96, HEIGHT - HEIGHT / 3))
            screen.blit(character_img, (WIDTH / 2 - 173, HEIGHT - HEIGHT / 3))

            self.frame_index += 1

        elif self.current_character == 2:
            t_enter = self.small_font.render("Wizard", False, (255, 255, 255))
            rect = t_enter.get_rect(center=(WIDTH / 2, HEIGHT / 3))
            screen.blit(t_enter, rect)
            # skill
            t_enter2 = self.small_font.render("Q Deal area damage, W Deal critical area damage, E Increase strength", False,
                                              (255, 255, 255))
            rect2 = t_enter2.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
            screen.blit(t_enter2, rect2)

            if self.current_sprite >= len(gWizard_image_list):
                self.current_sprite = 0

            if self.frame_index % 5 == 0:  # Change 5 to control animation speed
                self.current_sprite += 1  # Update frame index
                if self.current_sprite >= len(gWizard_image_list):
                    self.current_sprite = 0  # Reset frame index when it reaches the end

            # Display the current frame of the character image
            character_img = pygame.transform.scale(gWizard_image_list[self.current_sprite], (525, 250))
            #character_img = gWarrior_image_list[self.current_sprite]
            rect = character_img.get_rect(midtop=(WIDTH / 2 - 96, HEIGHT - HEIGHT / 3))
            screen.blit(character_img, (WIDTH / 2 - 250, HEIGHT - HEIGHT / 3 - 50))

            self.frame_index += 1


        """character_img = gRogue_image_list[self.current_character - 1]
        rect = character_img.get_rect(midtop=(WIDTH / 2 - 96, HEIGHT - HEIGHT / 3))
        screen.blit(character_img, (WIDTH / 2 - 96, HEIGHT - HEIGHT / 3))"""

    def Exit(self):
        pass