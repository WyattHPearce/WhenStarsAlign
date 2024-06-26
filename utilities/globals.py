# Standard Imports
import time

# Graphics Settings
ORIGINAL_SCREEN_WIDTH: int = 1600
ORIGINAL_SCREEN_HEIGHT: int = 900
current_screen_width: int = ORIGINAL_SCREEN_WIDTH
current_screen_height: int = ORIGINAL_SCREEN_HEIGHT
max_framerate: int = 60

# Framerate independence
target_framerate: int = 60
delta_time: float = 0.0
previous_time: float = time.perf_counter()

# Game Settings
TILESIZE: int = 30 # Size tiles will be displayed as in pixels

# Global Functions
def update_window_size_globals(game) -> None:
    """Updates screen size globals based on the current screen size."""
    global current_screen_width, current_screen_height
    current_screen_width = game.screen.get_width()
    current_screen_height = game.screen.get_height()
    print(f"Window resized to: {current_screen_width}x, {current_screen_height}y")

def update_delta_time() -> None:
    """Updates delta_time from time since previous function call"""
    global delta_time, previous_time
    current_time = time.perf_counter()
    delta_time = current_time - previous_time
    previous_time = current_time
    delta_time *= target_framerate