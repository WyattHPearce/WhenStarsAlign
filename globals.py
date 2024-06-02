# Standard Imports
import time
# Third-Party Imports
# Local Imports

# Graphics Settings
screen_width: int = 1280
screen_height: int = 720
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
    global screen_width, screen_height
    screen_width = game.screen.get_width()
    screen_height = game.screen.get_height()
    print(f"Window resized to: {screen_width}x, {screen_height}y")

def update_delta_time() -> None:
    """Updates delta_time from time since previous function call"""
    global delta_time, previous_time
    current_time = time.perf_counter()
    delta_time = current_time - previous_time
    previous_time = current_time
    delta_time *= target_framerate