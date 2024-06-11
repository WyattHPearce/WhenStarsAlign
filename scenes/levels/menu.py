# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from ..scene_template import SceneTemplate
from entity import Entity
from ui import UIElement

class Menu(SceneTemplate):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_color = (50,50,50)

    def init_objects(self) -> None:
        UIElement(
            [self.user_interface], 
            image=pygame.Surface((100,30)), 
            position=(globals.ORIGINAL_SCREEN_WIDTH/2, globals.ORIGINAL_SCREEN_HEIGHT/2), 
            origin='center'
        )
        UIElement([self.user_interface])
