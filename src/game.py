import sys 
import pygame
from consts import GAME_W, GAME_H, SCALE_FACTOR
from play_state import PlayState
from win_state import WinState
from edit_state import EditState
from assets import load_assets

class Game:
    def __init__(self):
        pygame.init()
        self.surf=pygame.Surface((GAME_W, GAME_H))
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((GAME_W*SCALE_FACTOR, GAME_H*SCALE_FACTOR), vsync=1)
        pygame.display.set_caption("SOCK")
        load_assets()
        self.running=True
        self.levels=self.load_levels()
        self.curr_level_index=0
        self.state=PlayState(self.levels[self.curr_level_index], self.switch_state)

    def load_levels(self):
        levels=[]
        with open("levels.txt", 'r') as file:
            level=[]
            for line in file:
                line=line.strip()
                if line=='{':
                    continue
                if line=='}':
                    levels.append(level)
                    level=[]
                    continue
                level.append(line)
        return levels

    def switch_state(self, state):
        if state=="next_level":
            if self.curr_level_index==len(self.levels)-1:
                self.curr_level_index=0
            else:
                self.curr_level_index+=1
            self.state=PlayState(self.levels[self.curr_level_index], self.switch_state)
        if state=="win": self.state=WinState(self.switch_state)
        if state=="play": self.state=PlayState(self.levels[self.curr_level_index], self.switch_state)
        if state=="edit": self.state=EditState(self.switch_state)

    def run(self):
        while self.running:
            dt=self.clock.tick(60) / 1000
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    self.running=False
                    break
                self.state.handle_input(e)
            self.state.update(dt)
            self.state.draw(self.surf)
            pygame.transform.scale(self.surf, self.screen.get_size(), self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
