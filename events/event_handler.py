# Standard Imports
# Third-Party Imports
import pygame
# Local Imports

events: list = None

def poll_events() -> None:
    global events
    events = pygame.event.get()

def quit_game() -> None:
    """Returns true if the close window button was pressed
    """
    for event in events:
            if event.type == pygame.QUIT:
                return True
    return False

def key_down(key) -> bool:
    """Returns true if the given keyboard key is pressed
    """
    for event in events:
        if event == pygame.KEYDOWN:
            if event.key == key:
                return True
    return False

def clicked(button_type: int = 1) -> bool:
    """Returns true if the given mouse button is pressed
    """
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == button_type:
                return True
    return False
            
def clicked_any() -> bool:
    """Returns true if any mouse button is pressed
    """
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
    return False