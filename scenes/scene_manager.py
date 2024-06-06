# Local Imports
from .levels.menu import Menu
from .levels.world1 import World1

current_scene: str = None
scenes: dict = None

def init_scenes(game) -> None:
    global scenes
    scenes = {
        'menu':Menu(game),
        'world1':World1(game)
    }

def set_scene(scene_name: str) -> None:
    """Set the current scene.

    Args:
        scene_name (str): Name of scene to be set as current.
    """
    global current_scene
    current_scene = scene_name

def update_scene(scene_name: str) -> None:
    """Updates the given scene.

    Args:
        scene_name (str): Name of scene to be updated.
    """
    scenes[scene_name].update()

def draw_scene(scene_name: str) -> None:
    """Draws the given scene.

    Args:
        scene_name (str): Name of scene to be drawn.
    """
    scenes[scene_name].draw()