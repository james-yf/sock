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
      ['e', 'b', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'b', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 's', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
      ['e', 'e', 'w', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
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
    def __init__(self, switch_state):
        self.start_direction="down"
        self.player=Player(facing=self.start_direction, assets=get_asset("player"))
        self.box=get_asset("box")
        self.grid=[row[:] for row in grid]
        self.storage_tiles=[]
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if self.is_tile_storage((ri, ci)):
                    self.storage_tiles.append((ri, ci))
        self.move_history=[]
        self.switch_state=switch_state
        self.won=False
        self.win_timer=0.0
        self.rewinding=False
        
    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_w or e.key==pygame.K_UP:
                move=self.move_player_in_dir("up")
                if move:
                    self.move_history.append(move)
                self.player.change_direction("up")
            if e.key==pygame.K_s or e.key==pygame.K_DOWN:
                move=self.move_player_in_dir("down")
                if move:
                    self.move_history.append(move)
                self.player.change_direction("down")
            if e.key==pygame.K_a or e.key==pygame.K_LEFT:
                move=self.move_player_in_dir("left")
                if move:
                    self.move_history.append(move)
                self.player.change_direction("left")
            if e.key==pygame.K_d or e.key==pygame.K_RIGHT:
                move=self.move_player_in_dir("right")
                if move:
                    self.move_history.append(move)
                self.player.change_direction("right")
            if e.key==pygame.K_u:
                if not self.move_history:
                    return
                self.undo_move()
            if e.key==pygame.K_r:
                self.rewinding=True

    def player_tile(self):
        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if col=='p':
                    return (ri, ci)
        return None

    def is_tile_wall(self, tile):
        ri, ci=tile
        return self.grid[ri][ci]=='w'

    def is_tile_box(self, tile):
        ri, ci=tile
        return self.grid[ri][ci]=='b'

    def is_tile_storage(self, tile):
        ri, ci=tile
        return self.grid[ri][ci]=='s'

    def move_player_in_dir(self, d):
        player_row, player_col=self.player_tile()
        if   d=="up"    : off_row, off_col = (- 1,   0)
        elif d=="down"  : off_row, off_col = (  1,   0)
        elif d=="left"  : off_row, off_col = (  0, - 1)
        else            : off_row, off_col = (  0,   1) 
        new_row, new_col=(player_row+off_row, player_col+off_col)
        
        if self.is_tile_wall((new_row, new_col)): 
            return None

        box_move=None
        if self.is_tile_box((new_row, new_col)):
            adj_tile=(new_row+off_row, new_col+off_col)
            if self.is_tile_wall(adj_tile) or self.is_tile_box(adj_tile):
                return None
            self.grid[adj_tile[0]][adj_tile[1]]='b'
            box_move=((new_row, new_col), adj_tile) 

        self.grid[player_row][player_col]='e'
        self.grid[new_row][new_col]='p'
        player_move=((player_row, player_col), (new_row, new_col))

        return (player_move, box_move) 

    def is_game_won(self):
        for tile in self.storage_tiles:
            ri, ci=tile
            if self.grid[ri][ci]!='b':
                return False
        return True

    def undo_move(self):
        player_move, box_move=self.move_history.pop()

        (player_src_row, player_src_col), (player_dest_row, player_dest_col)=player_move
        if not self.move_history:
            # maintain start direction for first move
            d=self.start_direction
        else:
            if player_dest_row-player_src_row==1:
                d_of_move="down"
                d_opp="up"
            elif player_dest_row-player_src_row==(-1):
                d_of_move="up"
                d_opp="down"
            elif player_dest_col-player_src_col==1:
                d_of_move="right"
                d_opp="left"
            else:
                d_of_move="left"
                d_opp="right"
            # assume no box_move has been made atp, so 
            # fine to travel in the opposition direction.
            d=d_opp

        self.grid[player_src_row][player_src_col]='p'
        self.grid[player_dest_row][player_dest_col]='e'

        if box_move:
            (box_src_row, box_src_col), (box_dest_row, box_dest_col)=box_move
            self.grid[box_src_row][box_src_col]='b'
            self.grid[box_dest_row][box_dest_col]='e'
            # box move is confirmed, so reset direction to travel direction. this is to make it
            # appear the player is pulling the box backwards, rather than moving away from it and
            # having it magically move.
            d=d_of_move

        self.player.change_direction(d)

    def update(self, dt):
        if self.rewinding:
            if not self.move_history:
                self.rewinding=False
                return
            self.undo_move()

        if self.won:
            self.win_timer-=dt
            if self.win_timer<=0:
                self.switch_state("win")
        else:
            if self.is_game_won():
                self.won=True
                self.win_timer=0.5

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
                if col=='b':
                    if (ri, ci) in self.storage_tiles:
                        surf.blit(self.box["at_storage"], (ci*TILE_SIZE, ri*TILE_SIZE))
                    else:
                        surf.blit(self.box["at_empty"], (ci*TILE_SIZE, ri*TILE_SIZE))
