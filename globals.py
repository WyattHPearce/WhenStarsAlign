# Graphics Settings
screen_width: int = 1280
screen_height: int = 720
max_framerate: int = 60

def update_window_size_globals(game) -> None:
    """Updates screen size globals based on the current screen size."""
    global screen_width, screen_height
    screen_width = game.screen.get_width()
    screen_height = game.screen.get_height()
    print(f"Window resized to: {screen_width}x, {screen_height}y")

# Game Settings
TILESIZE: int = 30 # Size tiles will be displayed as in pixels