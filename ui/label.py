# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from .ui_element import UIElement
from events import event_handler

class Label(UIElement):
    def __init__(self, groups, text: str, font: pygame.font.Font, color: tuple, size: tuple = (50,50), position: tuple = (0, 0), origin: str = 'topleft') -> None:
        """Label UI element with text.

        Args:
            groups (list): List of pygame.sprite.Group() groups
            text (str): The text to be displayed.
            font (pygame.font.Font): The font object.
            color (tuple): Color of the text.
            background_color (tuple, optional): Defaults to black. Background color of the label.
            size (tuple, optional): Defaults to (150,50). Width and height of element.
            position (tuple, optional): Defaults to (0, 0).
            origin (str, optional): The point on the image used as the anchor for positioning.
                Defaults to 'topleft'.
                Available options: 'topleft', 'bottomleft', 'topright', 'bottomright', 'midtop', 'midleft', 'midbottom', 'midright', 'center'
        """
        # Initialize UIElement with the text surface
        super().__init__(groups, size=size, position=position, origin=origin)

        # Store the text, font, and text color
        self.text = text
        self.font = font
        self.color = color

        # Set text
        self.set_text(self.text)

    def update(self) -> None:
        super().update()
        if event_handler.window_resized():
            self.set_text(self.text)

    def set_text(self, text: str) -> None:
        """Set the text of the label."""
        self.text = text
        self.image = self.font.render(text, False, self.color)
        self.rect.size = self.image.get_size()

    def set_font(self, font: pygame.font.Font) -> None:
        """Set the font of the label."""
        self.font = font
        self.set_text(self.text)

    def set_color(self, color: tuple) -> None:
        """Set the text color of the label."""
        self.color = color
        self.set_text(self.text)