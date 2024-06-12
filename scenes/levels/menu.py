# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from ..scene_template import SceneTemplate
from entity import Entity
from ui import *

class Menu(SceneTemplate):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_color = (40,40,55)

    def init_objects(self) -> None:

        test_element_3 = UIElement(
            [self.user_interface], 
            size=(100,30), 
            position=(globals.ORIGINAL_SCREEN_WIDTH/2, globals.ORIGINAL_SCREEN_HEIGHT/2), 
            origin='center'
        )

        test_element_2 = UIElement([self.user_interface])

        hello_text = Label(
            [self.user_interface],
            text='When Stars Align',
            font=fonts.roman_font,
            color=(0,0,0),
            size=(600,200),
            position=(globals.ORIGINAL_SCREEN_WIDTH/2, globals.ORIGINAL_SCREEN_HEIGHT/2-200),
            origin='center',
        )
