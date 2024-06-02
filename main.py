# Standard Imports
import sys
# Third-Party Imports
import pygame
# Local Imports
import globals as globals
from scene import Scene
import textures.texture_manager as texture_manager

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Create Screen
        self.screen: pygame.Surface = pygame.display.set_mode(
            (globals.screen_width, globals.screen_height), # Screen size
            pygame.RESIZABLE # Screen is resizable
        )

        # Initialize textures in texture manager
        texture_manager.init_textures()

        # Create clock
        self.clock = pygame.time.Clock()

        self.running: bool = True

        # Scenes
        self.dev_scene = Scene(self)

    def run(self) -> None:
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self) -> None:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Scene update
        self.dev_scene.update()

        # Enforcing max framerate
        self.clock.tick(globals.max_framerate)
        # Updating the display
        pygame.display.update()

    def draw(self) -> None:
        # Scene draw
        self.dev_scene.draw()

    def close(self) -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()