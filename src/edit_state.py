import pygame
from consts import GAME_W, GAME_H, TILE_SIZE, SCALE_FACTOR
from game_state import GameState
from assets import get_asset

class EditState(GameState):
    def __init__(self, switch_state):
        self.last_placed_tile=None
        self.grid_lines_toggled=True
        self.selected_obj=None
        self.player_tile=None
        self.player=get_asset("player")
        self.direction=None
        self.box=get_asset("box")["at_empty"]
        self.grid=[['e' for _ in range(20)] for _ in range(20)]
        self.switch_state=switch_state

    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_b:
                self.selected_obj='b'
            if e.key==pygame.K_w:
                self.selected_obj='w'
            if e.key==pygame.K_s:
                self.selected_obj='s'
            if e.key==pygame.K_e:
                self.selected_obj='e'
            if e.key==pygame.K_p:
                self.selected_obj='p'
                self.direction="down"
            if e.key==pygame.K_UP:
                self.direction="up"
            if e.key==pygame.K_DOWN:
                self.direction="down"
            if e.key==pygame.K_LEFT:
                self.direction="left"
            if e.key==pygame.K_RIGHT:
                self.direction="right"
            if e.key==pygame.K_SPACE:
                self.switch_state("play")
            if e.key==pygame.K_c:
                for ri, row in enumerate(self.grid):
                    for ci, col in enumerate(row):
                        self.grid[ri][ci]='e'
            if e.key==pygame.K_g:
                self.grid_lines_toggled=not self.grid_lines_toggled
            if e.key==pygame.K_RETURN or e.key==pygame.K_KP_ENTER:
                self.save_level()
                
        if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
            if self.selected_obj is None:
                return

            mouse_x, mouse_y=e.pos
            row, col=(mouse_y//SCALE_FACTOR//TILE_SIZE, mouse_x//SCALE_FACTOR//TILE_SIZE)

            if self.last_placed_tile:
                mods=pygame.key.get_mods()
                if mods & pygame.KMOD_SHIFT:
                    last_row, last_col=self.last_placed_tile
                    points=self.get_line_points(last_col, last_row, col, row) 
                    for row, col in points:
                       self.grid[row][col]=self.selected_obj

            if self.selected_obj=='p' and self.player_tile:
                p_row, p_col=self.player_tile
                self.grid[p_row][p_col]='e'

            self.grid[row][col]=self.selected_obj
            if self.selected_obj=='p': self.player_tile=(row, col)
            self.last_placed_tile=(row, col)

    # uses bresenham's line algo. do i understand it? no. but it works.
    def get_line_points(self, x0, y0, x1, y1):
        points=[]
        dx=abs(x1-x0)
        dy=abs(y1-y0)
        sx=1 if x0<x1 else -1
        sy=1 if y0<y1 else -1
        err=dx-dy
        while True:
            points.append((y0, x0))
            if (x0==x1 and y0==y1): break
            e2=2*err
            if (e2 > -dy): err-=dy; x0+=sx
            if (e2 <  dx): err+=dx; y0+=sy
        return points

    def save_level(self):
        with open("levels.txt", "a") as file:
            file.write("{\n")
            for row in self.grid:
                file.write(f"{"".join(row)}\n")
            file.write("}\n")

    def update(self, dt):
        pass

    def draw(self, surf):
        surf.fill((255,255,255))

        if self.grid_lines_toggled:
            color=(0,0,0)
            for i in range(20):
                pygame.draw.line(surf, color, (i*TILE_SIZE, 0), (i*TILE_SIZE, GAME_H))
                pygame.draw.line(surf, color, (0, i*TILE_SIZE), (GAME_W, i*TILE_SIZE))

        for ri, row in enumerate(self.grid):
            for ci, col in enumerate(row):
                if col=='b': 
                    surf.blit(self.box, (ci*TILE_SIZE, ri*TILE_SIZE))
                if col=='p': 
                    surf.blit(self.player[self.direction], (ci*TILE_SIZE, ri*TILE_SIZE))
                if col=='w': 
                    pygame.draw.rect(surf, (0,0,255), ((ci*TILE_SIZE, ri*TILE_SIZE), (TILE_SIZE, TILE_SIZE)))
                if col=='s': 
                    pygame.draw.circle(surf, (255,0,0), (ci*TILE_SIZE+TILE_SIZE//2, ri*TILE_SIZE+TILE_SIZE//2), TILE_SIZE//2)
