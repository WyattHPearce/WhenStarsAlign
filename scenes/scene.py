# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
from globals import *

class Scene:
    def __init__(self, game) -> None:
        self.game = game # Access to game

        self.background_color = (255,255,255)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.game.screen.fill((self.background_color))