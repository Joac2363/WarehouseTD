X = 0
Y = 1

import pygame
import random
class Enemy:
    def __init__(self, path, game):
        self.path = path 
        self.screen = game.screen
        self.hasFinished = False
        self.posIndex = 0
        self.pos = path[self.posIndex] #X,Y
        self.isAlive = True


        
    def move_enemy(self):
        # Move the enemy aslong as the enemy hasnt finished
        if random.randint(0,10000) == 1:
            self.image100P = pygame.image.load("sprites/enemies/easter_egg_enemy.png")
        if self.posIndex+1 >= len(self.path):
            self.hasFinished = True
        else:
            self.posIndex += 1
            self.pos = self.path[self.posIndex]
            self.rect.x = self.pos[X]*80
            self.rect.y = self.pos[Y]*80
            
    
    def update_self(self):
        if self.health <= 0:
            self.kill_self()
            return
        self._update_image()
        if not self.hasFinished:
            self._blit_self()

    def _update_image(self):
        if self.health < self.maxHealth * 1/3:
            self.image = self.image33P
        elif self.health < self.maxHealth * 2/3:
            self.image = self.image66P
        else:
            self.image = self.image100P

    def _blit_self(self):
        self.screen.blit(self.image, self.rect)


    def take_damage(self, dmg):
        self.health -= dmg
    
    def kill_self(self):
        self.isAlive = False
    
class Papkasse(Enemy):
    def __init__(self, path, game):
        super().__init__(path, game)
        self.image33P = pygame.image.load("sprites/enemies/enemy_1_stage_3.png")
        self.image66P = pygame.image.load("sprites/enemies/enemy_1_stage_2.png")
        self.image100P = pygame.image.load("sprites/enemies/enemy_1_stage_1.png")
        self.image = pygame.image.load("sprites/enemies/enemy_1_stage_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[X]*80
        self.rect.y = self.pos[Y]*80
    
        self.worth = 5 
        self.damage = 1
        self.health = 200
        self.maxHealth = self.health

class Plastickasse(Enemy):
    def __init__(self, path, game):
        super().__init__(path, game)
        self.image33P = pygame.image.load("sprites/enemies/enemy_2_stage_3.png")
        self.image66P = pygame.image.load("sprites/enemies/enemy_2_stage_2.png")
        self.image100P = pygame.image.load("sprites/enemies/enemy_2_stage_1.png")
        self.image = pygame.image.load("sprites/enemies/enemy_2_stage_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[X]*80
        self.rect.y = self.pos[Y]*80
        
        self.worth = 8
        self.damage = 2
        self.health = 800
        self.maxHealth = self.health


