# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from entity import Entity
from textures import texture_manager

class SceneTemplate:
    def __init__(self, game) -> None:
        self.game = game # Access to game
        self.background_color = (255,255,255)

        # Textures
        self.solo_textures = texture_manager.solo_textures
        self.block_atlas_textures = texture_manager.block_textures

        # Groups
        self.sprites = pygame.sprite.Group()
        self.user_interface = pygame.sprite.Group()

        self.init_objects()

    def init_objects(self) -> None:
        """Place object instances within this method."""
        pass

    def update(self) -> None:
        """Update the scene."""
        self.sprites.update()
        self.user_interface.update()

    def draw(self) -> None:
        """Draw the scene."""
        self.game.screen.fill((self.background_color))

        self.sprites.draw(self.game.screen)
        self.user_interface.draw(self.game.screen)