# Standard imports
# Third-Party Imports
import pygame
# Local Imports
import globals
from entity import Entity

# Custom Sprite Class
class UIElement(Entity):
    def __init__(self, groups, image=pygame.Surface((50, 50)), position: tuple = (0, 0), origin: str = 'topleft', color: tuple = (255, 255, 255)) -> None:
        super().__init__(groups, image, position)
        self.origin = origin
        self.color = color
        self.image.fill(self.color)

        # Resizing
        self.original_position = pygame.math.Vector2(position)
        self.original_size = self.image.get_size()
        self.original_screen_size = (globals.screen_width, globals.screen_height)

    def update(self) -> None:
        """Augmentation of super class update method."""
        super().update()
        self.scale_to_screen((globals.screen_width, globals.screen_height))
    
    def scale_to_screen(self, new_screen_size: tuple) -> None:
        """Takes a new screensize and rescales / re-positions the UIElement.

        Args:
            new_screen_size (tuple): Screen size to be rescaled to.
        """
        new_width, new_height = new_screen_size
        original_width, original_height = self.original_screen_size
        
        # Calculate scaling factors
        scale_x = new_width / original_width
        scale_y = new_height / original_height
        
        # Scale position
        self.position.x = self.original_position.x * scale_x
        self.position.y = self.original_position.y * scale_y
        
        # Scale size
        new_size = (
            int(self.original_size[0] * scale_x), 
            int(self.original_size[1] * scale_y)
        )
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect.size = new_size

        # Setting origin of position
        if self.origin == 'topleft':
            self.rect.topleft = self.position
        if self.origin == 'center':
            self.rect.center = self.position