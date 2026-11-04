import pygame
from game_state import GameState
from assets import get_asset
from consts import GAME_W, GAME_H, TILE_SIZE
from player import Player

# keeping the grid here for now until i add more levels. will make a level editor when that time comes. 
grid=[
      ['p', 'w', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 's', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 's', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
]

class PlayState(GameState):
    def __init__(self):
        self.player=Player(facing="down", assets=get_asset("player"))
        self.grid=grid
        self.storage_tiles=[]
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if self.is_tile_storage((ri, ci)):
                    self.storage_tiles.append((ri, ci))
        
    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_w or e.key==pygame.K_UP:
                player_row, player_col=self.player_tile()
                new_row, new_col=player_row-1, player_col
                if self.is_tile_wall((new_row, new_col)):
                    return
                self.player.change_direction("up")
                self.grid[player_row][player_col]='e'
                self.grid[new_row][new_col]='p'
            if e.key==pygame.K_s or e.key==pygame.K_DOWN:
                player_row, player_col=self.player_tile()
                new_row, new_col=player_row+1, player_col
                if self.is_tile_wall((new_row, new_col)):
                    return
                self.player.change_direction("down")
                self.grid[player_row][player_col]='e'
                self.grid[new_row][new_col]='p'
            if e.key==pygame.K_a or e.key==pygame.K_LEFT:
                player_row, player_col=self.player_tile()
                new_row, new_col=player_row, player_col-1
                if self.is_tile_wall((new_row, new_col)):
                    return
                self.player.change_direction("left")
                self.grid[player_row][player_col]='e'
                self.grid[new_row][new_col]='p'
            if e.key==pygame.K_d or e.key==pygame.K_RIGHT:
                player_row, player_col=self.player_tile()
                new_row, new_col=player_row, player_col+1
                if self.is_tile_wall((new_row, new_col)):
                    return
                self.player.change_direction("right")
                self.grid[player_row][player_col]='e'
                self.grid[new_row][new_col]='p'

    def player_tile(self):
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if col=='p':
                    return (ri, ci)
        return None

    def is_tile_wall(self, tile):
        ri, ci=tile
        return self.grid[ri][ci]=='w'

    def is_tile_storage(self, tile):
        ri, ci=tile
        return self.grid[ri][ci]=='s'

    def update(self, dt):
        pass

    def draw(self, surf):
        surf.fill((0,0,0))
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if col=='w':
                    pygame.draw.rect(surf, (0,0,255), ((ci*TILE_SIZE, ri*TILE_SIZE), (TILE_SIZE, TILE_SIZE)))
                if (ri, ci) in self.storage_tiles:
                    pygame.draw.circle(surf, (255,0,0), (ci*TILE_SIZE+TILE_SIZE//2, ri*TILE_SIZE+TILE_SIZE//2), TILE_SIZE//2)
                if col=='p':
                    self.player.draw(surf, (ci*TILE_SIZE, ri*TILE_SIZE))
