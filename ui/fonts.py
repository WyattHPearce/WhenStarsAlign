# Third-Party Imports
import pygame

arial_font = None
roman_font = None

def init_fonts() -> None:
    global arial_font, roman_font
    arial_font = pygame.font.SysFont("Arial", 22)
    roman_font = pygame.font.SysFont("Times New Roman", 22)