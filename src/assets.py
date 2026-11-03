import pygame
from pathlib import Path
from consts import TILE_SIZE

ASSETS=Path(__file__).parent.parent / "assets"
IMGS=ASSETS / "imgs"

assets={}

def load_assets():
    player_sheet=pygame.image.load(IMGS / "player_sheet.png").convert_alpha()
    assets["player"]={
        "right": extract_tile(player_sheet, 0),
        "left": extract_tile(player_sheet, 1),
        "down": extract_tile(player_sheet, 2),
        "up": extract_tile(player_sheet, 3)
    }

def get_asset(name):
    return assets[name]

def extract_tile(tilesheet, col_off):
    return tilesheet.subsurface((col_off*TILE_SIZE, 0), (TILE_SIZE, TILE_SIZE)) 
