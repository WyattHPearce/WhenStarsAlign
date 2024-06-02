# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals

events: list = []
event_flags: dict = {
    'has_quit': False,
    'window_resized': False,
    'key_down': {},
    'clicked': {}
}

def poll_events() -> None:
    global events, event_flags
    events = pygame.event.get()

    # Reset event flags
    event_flags['has_quit'] = False
    event_flags['window_resized'] = False
    event_flags['key_down'] = {}
    event_flags['clicked'] = {}

    # Event loop
    for event in events:
        if event.type == pygame.QUIT:
            # Quit
            event_flags['has_quit'] = True
        elif event.type == pygame.VIDEORESIZE:
            # Resizing
            event_flags['window_resized'] = True
        elif event.type == pygame.KEYDOWN:
            # Key Down
            event_flags['key_down'][event.key] = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button Down
            event_flags['clicked'][event.button] = True

def has_quit() -> bool:
    """Returns true if the quit event is detected."""
    return event_flags['has_quit']

def window_resized() -> bool:
    """Returns true if the window resize event is detected."""
    return event_flags['window_resized']

def key_down(key: int) -> bool:
    """Returns true if the given keyboard key is pressed."""
    return event_flags['key_down'].get(key, False)

def clicked(button_type: int = 1) -> bool:
    """Returns true if the given mouse button is pressed."""
    return event_flags['clicked'].get(button_type, False)