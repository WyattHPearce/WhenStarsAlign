# Standard Imports
import sys
# Third-Party Imports
import pygame
# Local Imports
from utilities import globals
from textures import texture_manager
from events import event_handler
from scenes import scene_manager
from ui import fonts

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Create Screen 
        self.screen: pygame.Surface = pygame.display.set_mode(
            (globals.ORIGINAL_SCREEN_WIDTH,globals.ORIGINAL_SCREEN_HEIGHT), # Screen size
            pygame.RESIZABLE, # Screen is resizable
            pygame.SCALED,
            vsync=1
        )
        pygame.display.set_caption('When Stars Align') # Game title

        # Initialize textures in texture manager
        texture_manager.init_textures()

        # Initialize fonts in the ui.font module
        fonts.init_fonts()

        # Initialize game scenes
        scene_manager.init_scenes(self)
        scene_manager.set_scene('menu')

        # Create clock
        self.clock = pygame.time.Clock()

        # Gameloop and Framerate Independence
        self.running: bool = True

    def run(self) -> None:
        while self.running:
            event_handler.handle_events(self)
            self.update()
            self.draw()
        self.close()

    def update(self) -> None:
        # Enforcing max framerate
        self.clock.tick(globals.max_framerate)

        # Update Delta Time
        globals.update_delta_time()

        # Scene update
        scene_manager.update_scene(scene_manager.current_scene)

        # Updating the display
        pygame.display.update()

    def draw(self) -> None:
        # Scene draw
        scene_manager.draw_scene(scene_manager.current_scene)

    def close(self) -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":

    game = Game()
    game.run()