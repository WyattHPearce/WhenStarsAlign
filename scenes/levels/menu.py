# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals
from scenes.scene_template import SceneTemplate
from entity import Entity

class Menu(SceneTemplate):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_color = (255,255,200)

    def init_objects(self) -> None:
        pass