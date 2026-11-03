import pygame
from game_state import GameState
from assets import get_asset
from consts import GAME_W, GAME_H, TILE_SIZE
from player import Player

class PlayState(GameState):
    def __init__(self):
        self.player=Player(x=0, y=0, facing="down", assets=get_asset("player"))
        
    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_w or e.key==pygame.K_UP:
                self.player.move_up()
            if e.key==pygame.K_s or e.key==pygame.K_DOWN:
                self.player.move_down()
            if e.key==pygame.K_a or e.key==pygame.K_LEFT:
                self.player.move_left()
            if e.key==pygame.K_d or e.key==pygame.K_RIGHT:
                self.player.move_right()

    def update(self, dt):
        pass

    def draw(self, surf):
        surf.fill((0,0,0))
        self.player.draw(surf)
