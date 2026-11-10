import pygame
from consts import GAME_W, GAME_H
from game_state import GameState

class WinState(GameState):
    def __init__(self, switch_state):
        self.complete_font=pygame.font.Font(None, 32)
        self.complete_txt=self.complete_font.render("Level Complete!", True, (255,255,255)) 
        self.complete_txt_w, self.complete_txt_h=self.complete_txt.get_size()
        self.prompt_font=pygame.font.Font(None, 24)
        self.restart_txt=self.prompt_font.render("Press R to restart", True, (255,255,255)) 
        self.restart_txt_w, self.restart_txt_h=self.restart_txt.get_size()
        self.next_txt=self.prompt_font.render("Press SPACE for next level", True, (255,255,255)) 
        self.next_txt_w, self.next_txt_h=self.next_txt.get_size()
        self.switch_state=switch_state

    def handle_input(self, e):
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_r:
                self.switch_state("play") 
            if e.key==pygame.K_SPACE:
                self.switch_state("next_level")

    def update(self, dt):
        pass

    def draw(self, surf):
        surf.fill((0,0,0))
        surf.blit(self.complete_txt, (GAME_W//2-self.complete_txt_w//2, GAME_H//2-self.complete_txt_h//2))
        surf.blit(self.restart_txt, (GAME_W//2-self.restart_txt_w//2, GAME_H//2+self.complete_txt_h//1))
        surf.blit(self.next_txt, (GAME_W//2-self.next_txt_w//2, GAME_H//2+self.complete_txt_h+self.restart_txt_h))
