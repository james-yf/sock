import pygame
from consts import TILE_SIZE

class Player:
    def __init__(self, x, y, facing, assets):
        self.facing=facing
        self.rect=pygame.Rect((x, y), (TILE_SIZE, TILE_SIZE))
        self.assets=assets

    def move_up(self):
        self.rect.y-=TILE_SIZE
        self.facing="up"

    def move_down(self):
        self.rect.y+=TILE_SIZE
        self.facing="down"

    def move_left(self):
        self.rect.x-=TILE_SIZE
        self.facing="left"

    def move_right(self):
        self.rect.x+=TILE_SIZE
        self.facing="right"

    def draw(self, surf):
        surf.blit(self.assets[self.facing], (self.rect.x, self.rect.y))
