import pygame
import math
class Tile:
    def __init__(self, game, x, y):
        self.image = pygame.image.load("sprites/tiles/unknown tile.png")
        self.screen = game.screen
        self.x = x
        self.y = y
        
        self.rect = self.image.get_rect()
        self.rect.x = x*80
        self.rect.y = y*80

    def blit_self(self):
        self.screen.blit(self.image, self.rect)
        
class Grass(Tile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("sprites/tiles/paths/base_tile.png")
        
class Path(Tile):
    def __init__(self, game, x, y, path: list):
        super().__init__(game, x, y)
        self.x = x
        self.y = y
        self.path = path
        self.image = pygame.image.load("sprites/tiles/paths/base_tile.png")
        #self.image = pygame.transform.rotate(self.image, 90)
        
        directions = self.path_direction()
        if len(directions) > 0:
            if directions[0][0] == 0 == directions[1][0]:
                if directions[0][1] < 0:
                    self.image = pygame.image.load("sprites/tiles/paths/north_south.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/south_north.png")
                    
            elif directions[0][1] == 0 == directions[1][1]:
                if directions[1][0] < 0:
                    self.image = pygame.image.load("sprites/tiles/paths/east_west.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/west_east.png")
            
            #X difference to Y difference
            elif directions[0][0] < 0:
                if directions[1][1] > 0:
                    self.image = pygame.image.load("sprites/tiles/paths/west_south.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/west_north.png")
            
            elif directions[0][0] > 0:
                if directions[1][1] > 0:
                    self.image = pygame.image.load("sprites/tiles/paths/east_south.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/east_north.png")

            #Y difference to X difference
            elif directions[0][1] > 0:
                if directions[1][0] < 0:
                    self.image = pygame.image.load("sprites/tiles/paths/south_west.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/south_east.png")
            
            elif directions[0][1] < 0:
                if directions[1][0] < 0:
                    self.image = pygame.image.load("sprites/tiles/paths/north_west.png")
                else:
                    self.image = pygame.image.load("sprites/tiles/paths/north_east.png")
        
    def path_direction(self):
        path_difference = []
        if [self.x, self.y] in self.path:
            pos = self.path.index([self.x, self.y])
            
            if pos > 0 and pos < len(self.path)-1 :
                path_difference.append([self.path[pos-1][0] - self.x, self.path[pos-1][1] - self.y])
                path_difference.append([self.path[pos+1][0] - self.x, self.path[pos+1][1] - self.y])
                #Path difference, is where the prevoius or next tile is compared to the currrent tile.
                #That means [0,1] is prevous tile is same level on the x axis, and +1 on the y axis
            elif pos == 0:
                path_difference.append([-1,0])
                path_difference.append([self.path[pos+1][0] - self.x, self.path[pos+1][1] - self.y])
            else:
                path_difference.append([self.path[pos-1][0] - self.x, self.path[pos-1][1] - self.y])
                path_difference.append([1,0])

            
        return path_difference

#class Path(Tile):
    
        
    
