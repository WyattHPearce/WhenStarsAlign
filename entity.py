# Standard imports
# Third-Party Imports
import pygame
# Local Imports
import globals as globals

# Custom Sprite Class
class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((globals.TILESIZE, globals.TILESIZE)), position: tuple = (0,0)) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = image
        self.rect: pygame.rect = image.get_rect(topleft = position)
        
    def update(self) -> None:
        pass

