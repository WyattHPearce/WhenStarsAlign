# Standard Imports
# Third-Party Imports
# Local Imports
from scenes.levels.menu import Menu
from scenes.levels.world import World

current_scene: str = None
scenes: dict = None

def init_scenes(game) -> None:
    global scenes
    scenes = {
        'menu':Menu(game),
        'world':World(game)
    }

def set_scene(scene_name: str) -> None:
    global current_scene
    current_scene = scene_name

def update_scene(scene_name: str) -> None:
    scenes[scene_name].update()

def draw_scene(scene_name: str) -> None:
    scenes[scene_name].draw()