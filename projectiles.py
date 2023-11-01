import enemies
import pygame
import math
class Projectile:
    def __init__(self, grid_pos, enemy, path:list, game):
        if not isinstance(enemy, enemies.Enemy):
            raise TypeError("Input must be an enemy_class")

        self.done = False
        self.grid_pos = grid_pos
        self.enemy = enemy
        self.path = path
        self.screen = game.screen
        self.speed = 10
        self.pos = [self.grid_pos[0]*80 + 40, self.grid_pos[1]*80 + 40]
        self.original_pos = self.pos
        self.image = pygame.image.load("sprites/projectiles/box_cutter_projectile.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rotated_image = self.image.copy()
        self.rotation = 0
        self.coords = [0, 0]
        

        self._update_rect()
        

    def update_self(self):

        self._move_projectile()
        self._check_for_enemy()
        self._update_rect()
        self._rotate()
        self._blit_self()

    def _move_projectile(self):
        self.coords = [(self.enemy.pos[0]*80+40)-self.pos[0],(self.enemy.pos[1]*80+40)-self.pos[1]] #Get's the difference between the current position in pixels, and the enemy's grid position in pixels
        hyp = math.hypot(self.coords[0], self.coords[1]) #Hypotenuse between arrow and target calculated
        
        # Unless the distance is 0 it updates the position of the arrow relative to the angle
        if hyp != 0:
            cos = self.coords[0]/hyp
            sin = self.coords[1]/hyp

            self.pos[0] += cos * self.speed
            self.pos[1] += sin * self.speed
            

    def _update_rect(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
    def _check_for_enemy(self):
        is_at_enemy_x = self.enemy.pos[0] * 80 <= self.pos[0] <= self.enemy.pos[0]*80 + 80
        is_at_enemy_y = self.enemy.pos[1] * 80 <= self.pos[1] <= self.enemy.pos[1]*80 + 80
        if is_at_enemy_x and is_at_enemy_y:
            #Do something
            self.enemy.take_damage(100)
            self.done = True
            
    
    def _rotate(self):
        original_rect = self.image.get_rect() 
        
        # To be honest I'm not quite sure what i was thinking at the time i wrote this 
        #       Negative atan towards the enemy. It just works  ¯\_(ツ)_/¯
        rot = -math.degrees(math.atan2(self.coords[1], self.coords[0]))

        self.rotated_image = pygame.transform.rotate(self.image, rot+180)   #Rotates the image the rotation plus 180 degrees to compensate for image orientation
        rotated = self.rotated_image.get_rect()
        self.rotation = rot
        dif = [original_rect[2]-rotated[2], original_rect[3]-rotated[3]]    #Difference in widt, height, in the rect
        
        #Compensates for the picture shifting
        self.rect.x += dif[0]
        self.rect.y += dif[1]
        
        
        
    def _blit_self(self):
        self.screen.blit(self.rotated_image, self.rect)
        

class ScissorArrow(Projectile):
    def __init__(self, grid_pos, enemy, path: list, game):
        super().__init__(grid_pos, enemy, path, game)
        self.speed = 15
        self.image = pygame.image.load("sprites/projectiles/Tower_2_projectile.png")
        self.image = pygame.transform.rotate(self.image, 315)
        self.rect = self.image.get_rect()
        self.rotated_image = self.image.copy() # Deep copy not needed

class KnifeArrow(Projectile):
    def __init__(self, grid_pos, enemy, path: list, game):
        super().__init__(grid_pos, enemy, path, game)
        self.speed = 15
        self.image = pygame.image.load("sprites/projectiles/box_cutter_projectile.png")
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rotated_image = self.image.copy() # Deep copy not needed
