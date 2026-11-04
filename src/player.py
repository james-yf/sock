import pygame
from consts import TILE_SIZE

class Player:
    def __init__(self, facing, assets):
        self.facing=facing
        self.assets=assets

    def change_direction(self, d):
        self.facing=d

    def draw(self, surf, pos):
        surf.blit(self.assets[self.facing], pos)
