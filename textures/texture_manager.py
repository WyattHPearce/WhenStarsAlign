# Standard Imports
# Third-Party Imports
import pygame
# Local Imports
import globals
import textures.texture_data as texture_data

solo_textures: dict = None
block_textures: dict = None

def init_textures():
    """Initializes module texture variables using module functions
    """
    global solo_textures, block_textures
    if solo_textures is None:
        solo_textures = gen_solo_textures(texture_data.solo_texture_data)
    if block_textures is None:
        block_textures = gen_atlas_textures(texture_data.block_texture_data, 'resources/block_atlas.png', 16, 16)

def gen_solo_textures(data: dict) -> dict:
    """Generates individual textures from texture data and returns them in a dictionary
    """
    textures: dict = {}

    # Populates textures to be returned
    for name, data in data.items():
        texture: pygame.Surface = pygame.image.load(data['file_path']).convert_alpha()
        textures[name] = pygame.transform.scale(texture, (data['size'][0] * globals.TILESIZE, data['size'][1] * globals.TILESIZE))
    
    return textures

def gen_atlas_textures(data: dict, atlas_file_path: str, atlas_width: int, atlas_height: int) -> dict:
    """Generates textures from an atlas image and returns them in a dictionary
    """
    textures: dict = {}

    # Conforms atlas image size to tilesize
    atlas_image: pygame.Surface = pygame.image.load(atlas_file_path).convert_alpha()
    atlas_image = pygame.transform.scale(atlas_image, (globals.TILESIZE*atlas_width, globals.TILESIZE*atlas_height))

    # Populates textures to be returned
    for name, data in data.items():
        textures[name] = pygame.Surface.subsurface(
            atlas_image, 
            pygame.Rect(
                (data['position'][0]*globals.TILESIZE, data['position'][1]*globals.TILESIZE), # Position
                (data['size'][0] * globals.TILESIZE, data['size'][1] * globals.TILESIZE) # Size
            )
        )

    return textures