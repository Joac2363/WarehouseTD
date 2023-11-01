import sys
import pygame
from settings import Settings


class Player_input:
    def __init__(self):
        self.settings = Settings()
        
        self.mouse = [0, 0, False]
        pygame.mouse.set_visible(False)
        self.image = pygame.image.load("sprites/misc/mouse.png")
        #Aims to make self.mouse_grid_pos more readable
        self.tile_dim = self.settings.tile_dim
        self.mouse_grid_pos = [self.mouse[0] // self.tile_dim[0], self.mouse[1] // self.tile_dim[1]]


    def update(self):
        self._get_mouse_pos()
        self._get_input_events()

    def _get_mouse_pos(self):
        pos = pygame.mouse.get_pos()
        self.mouse[0] = pos[0]
        self.mouse[1] = pos[1]
        self.mouse_grid_pos = [pos[0] // self.tile_dim[0], pos[1] // self.tile_dim[1]]

    def _get_input_events(self):
        self.mouse[2] = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.K_q:
                sys.exit()
            
            #Placeholder for future keybindings
            #elif event.type == pygame.//Key//:
                #Do something
                
                        
            #This check should be at the buttom
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse[2] = True

