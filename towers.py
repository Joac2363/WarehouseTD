import pygame
import math
from clock import Clock

class Tower:
    def __init__(self, game, x, y):
        self.screen = game.screen
        self.game = game
        self.path = game.path_finder.path
        self.x = x
        self.y = y
        self.gridPos = [x,y]
        self.targetCoords = None

        self.clock = Clock()

        self.should_attack = False
        self.fireRate = None
        self.damage = None
        self.range = None

    def _blit_self(self):
        self.screen.blit(self.image, self.rect)
    
    def update_self(self, grid):
        self._blit_self()
        # Fire every 𝒻𝒾𝓇𝑒𝓇𝒶𝓉𝑒 seconds
        if self.clock.get_time_since_last() > self.fireRate:
            self.clock.reset_lasttime()
            self._use_attack(grid)
        else:
            self.should_attack = False

    def _use_attack(self, grid):
        self._update_target_enemy(grid)
        if self.targetCoords is not None:
            self.should_attack = True

    def _update_target_enemy(self, grid):
        for tile in reversed(self.path):
            x = tile[0]
            y = tile[1]
            if type(grid[y][x]) != type(""):
                distTowerToEnemy = math.sqrt((x - self.x)**2 + (y - self.y)**2)
                if distTowerToEnemy <= self.range:
                    self.targetCoords = [x,y]
                    return
        self.targetCoords = None


class Scissor(Tower):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("sprites/towers/tower 2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x*80
        self.rect.y = y*80 - 80

        self.fireRate = 1
        self.damage = 50
        self.range = 3

class Knife(Tower):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("sprites/towers/box_cutter_tower_state_one.png")
        self.rect = self.image.get_rect()
        self.rect.x = x*80
        self.rect.y = y*80 - 80

        self.fireRate = 0.75
        self.damage = 0
        self.range = 1000