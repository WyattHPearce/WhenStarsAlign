# Standard imports
# Third-Party Imports
import pygame
# Local Imports
import globals

# Custom Sprite Class
class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((globals.TILESIZE, globals.TILESIZE)), position: tuple=(0,0)) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = image
        self.position = pygame.math.Vector2(position)
        self.rect: pygame.Rect = image.get_rect(topleft = self.position)
        
    def update(self) -> None:
        """Overrides pygame.sprite.Sprite update method. Can be called from sprite group names."""
        # Prevents stutter from delta_time float precision issues
        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y)
        )

