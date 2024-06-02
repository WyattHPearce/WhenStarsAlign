# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals
from scenes.scene_template import SceneTemplate
from entity import Entity
import events.event_handler as event_handler

class World1(SceneTemplate):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background_color = (0,0,0)

    def init_objects(self) -> None:
        super().init_objects()
        self.block = Entity(
            [self.sprites], 
            image=self.block_atlas_textures['grass'], 
            position=(globals.TILESIZE,globals.screen_height/2)
        )

    def update(self) -> None:
        super().update()
        self.block.rect.x += (3 * globals.delta_time)