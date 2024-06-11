# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from entity import Entity

# Custom Sprite Class
class UIElement(Entity):
    def __init__(self, groups, image=pygame.Surface((50, 50)), position: tuple = (0, 0), origin: str = 'topleft') -> None:
        """Base UI element/ Handles basic scaling and screen snapping.

        Args:
            groups (list): List of pygame.sprite.Group() groups
            image (pygame.Surface, optional): Defaults to pygame.Surface((50, 50)).
            position (tuple, optional): Defaults to (0, 0).
            origin (str, optional): The point on the image used as the anchor for positioning.
                Defaults to 'topleft'.
                Available options: 'topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center'
        """
        super().__init__(groups, image, position)
        self.origin = origin

        # Temp coloring for visual testing
        self.image.fill((255,255,255))

        # Resizing
        self.original_position = pygame.math.Vector2(position)
        self.original_size = self.image.get_size()

    def update(self) -> None:
        """Augmentation of super class update method."""
        super().update()
        self.scale_to_screen((globals.current_screen_width, globals.current_screen_height))
    
    def scale_to_screen(self, new_screen_size: tuple) -> None:
        """Takes a new screensize and rescales / re-positions the UIElement based on original screen sizes.

        Args:
            new_screen_size (tuple): Screen size to be rescaled to.
        """
        original_screen_width = globals.ORIGINAL_SCREEN_WIDTH
        original_screen_height = globals.ORIGINAL_SCREEN_HEIGHT

        new_screen_width, new_screen_height = new_screen_size

        # Calculate scaling factors
        scale_x = new_screen_width / original_screen_width
        scale_y = new_screen_height / original_screen_height

        # Scale the position normally
        new_position = (self.original_position[0] * scale_x, self.original_position[1] * scale_y)

        # Choose the smaller scaling factor to maintain aspect ratio for size
        scale = min(scale_x, scale_y)

        # Scale the size
        new_width = int(self.original_size[0] * scale)
        new_height = int(self.original_size[1] * scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        # Update the rect size
        self.rect.size = self.image.get_size()

        # Update the rect position based on the origin
        setattr(self.rect, self.origin, new_position)