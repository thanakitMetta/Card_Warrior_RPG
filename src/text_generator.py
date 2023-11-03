import pygame
import sys
import time
from src.constants import *
from src.Dependencies import *
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Function to display text character by character
class TextGenerator:
    def __init__(self, text, font, x, y, delay=0.1):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.delay = delay
        self.text_index = 0
        self.fully_displayed = False
        self.typing_sound = gSounds['Retro_Single_v6']

    def text_generation(self):

        while self.text_index <= len(self.text):
            time.sleep(self.delay)
            #sound
            self.typing_sound.play()
            partial_text = self.text[:self.text_index]
            text_surface = self.font.render(partial_text, True, (255, 255, 255))
            screen.blit(text_surface, (self.x, self.y))
            pygame.display.update()

            self.text_index += 1

        if self.text_index > len(self.text):
            self.fully_displayed = True
            time.sleep(1)  # Wait for 1 second after text fully appears

        return self.fully_displayed

    def text_generation_reset(self):
        self.fully_displayed = False
        self.text_index = 0