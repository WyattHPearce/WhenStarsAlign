# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals as globals
from scenes.scene_template import SceneTemplate
from entity import Entity

class Level1(SceneTemplate):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_color = (200,255,255)

    def init_objects(self) -> None:
        Entity(
            [self.sprites], 
            image=self.block_atlas_textures['dirt1'], 
            position=(0, 0)
        )