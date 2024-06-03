# Standard Imports
import sys
# Third-Party Imports
import pygame
# Local Imports
import globals
import textures.texture_manager as texture_manager
import events.event_handler as event_handler
# Scenes
import scenes.scene_manager as scene_manager

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Create Screen
        self.screen: pygame.Surface = pygame.display.set_mode(
            (globals.screen_width, globals.screen_height), # Screen size
            pygame.RESIZABLE, # Screen is resizable
            pygame.SCALED,
            vsync=1
        )
        pygame.display.set_caption('When Stars Align') # Game title

        # Initialize textures in texture manager
        texture_manager.init_textures()

        # Create clock
        self.clock = pygame.time.Clock()

        # Gameloop and Framerate Independence
        self.running: bool = True

        # Initialize game scenes
        scene_manager.init_scenes(self)
        scene_manager.set_scene('menu')

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