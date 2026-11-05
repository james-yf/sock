import pygame
from consts import GAME_W, GAME_H
from game_state import GameState

class WinState(GameState):
    def __init__(self, switch_state):
        self.complete_font=pygame.font.Font(None, 32)
        self.complete_txt=self.complete_font.render("Level Complete!", True, (255,255,255)) 
        self.complete_txt_w, self.complete_txt_h=self.complete_txt.get_size()
        self.prompt_font=pygame.font.Font(None, 24)
        self.prompt_txt=self.prompt_font.render("Press R to restart", True, (255,255,255)) 
        self.prompt_txt_w, self.prompt_txt_h=self.prompt_txt.get_size()
        self.switch_state=switch_state

    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_r:
                self.switch_state("play") 

    def update(self, dt):
        pass

    def draw(self, surf):
        surf.fill((0,0,0))
        surf.blit(self.complete_txt, (GAME_W//2-self.complete_txt_w//2, GAME_H//2-self.complete_txt_h//2))
        surf.blit(self.prompt_txt, (GAME_W//2-self.prompt_txt_w//2, GAME_H//2+self.complete_txt_h//1))
