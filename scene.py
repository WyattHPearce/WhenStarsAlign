# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals as globals
from entity import Entity
import textures.texture_manager as texture_manager

class Scene:
    def __init__(self, game) -> None:
        self.game = game # Access to game
        self.background_color = (255,255,255)

        # Textures
        self.solo_textures = texture_manager.solo_textures
        self.block_atlas_textures = texture_manager.block_textures

        # Groups
        self.sprites = pygame.sprite.Group()

        print(self.game.screen)

        Entity([self.sprites], image=self.block_atlas_textures['dirt2'])

    def update(self) -> None:
        self.sprites.update()

    def draw(self) -> None:
        self.game.screen.fill((self.background_color))

        self.sprites.draw(self.game.screen)