# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals
from entity import Entity
import textures.texture_manager as texture_manager

class SceneTemplate:
    def __init__(self, game) -> None:
        self.game = game # Access to game
        self.background_color = (255,255,255)

        # Textures
        self.solo_textures = texture_manager.solo_textures
        self.block_atlas_textures = texture_manager.block_textures

        # Groups
        self.sprites = pygame.sprite.Group()

        self.init_objects()

    def init_objects(self) -> None:
        pass

    def update(self) -> None:
        self.sprites.update()

    def draw(self) -> None:
        self.game.screen.fill((self.background_color))

        self.sprites.draw(self.game.screen)