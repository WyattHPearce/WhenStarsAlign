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
        self.box = UIElement(
            [self.user_interface], 
            image=pygame.Surface((100,30)), 
            position=(globals.screen_width/2, globals.screen_height/2), 
            origin='center',
            color=(255,255,255)
        )
