import sys 
import pygame
from consts import GAME_W, GAME_H
from play_state import PlayState
from assets import load_assets

SCALE_FACTOR=2

class Game:
    def __init__(self):
        pygame.init()
        self.surf=pygame.Surface((GAME_W, GAME_H))
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((GAME_W*SCALE_FACTOR, GAME_H*SCALE_FACTOR), vsync=1)
        load_assets()
        self.running=True
        self.state=PlayState()

    def switch_state(self, state):
        pass

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
