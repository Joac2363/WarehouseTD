#----------------------------------------------------------
#                        Imports
#----------------------------------------------------------

import sys # Used by boringstuff.py
import pygame #Used throughout multiple files
import time #Used in clock.py
import copy  # Used throughout multiple files
import colorsys #Used by menu.py
from tiles import Tile, Grass, Path
from towers import Tower, Scissor, Knife
from enemies import Enemy, Papkasse, Plastickasse
from projectiles import Projectile, KnifeArrow, ScissorArrow
from clock import Clock
from boringstuff import Player_input
from menu import Menu, MenuButton, StartScreen
from settings import Settings 
from settings import Path_finder 
import errors

#Something from the internet that should work:
import ctypes #Used in TD.py
ctypes.windll.user32.SetProcessDPIAware()


#----------------------------------------------------------
#                        The Game
#----------------------------------------------------------


X = 0
Y = 1
class TD:
    def __init__(self, gridIndex):
        pygame.init()
        
        self.settings = Settings()


        #Useless stuff
        self.screen = pygame.display.set_mode((1920, 1090), pygame.FULLSCREEN|pygame.NOFRAME)
        self.screen_height = self.screen.get_rect().height
        self.screen_width = self.screen.get_rect().width
        self.input = Player_input()

        #Grid
        self.gridIndex = gridIndex

        #Enemies
        self.all_enemies = []

        #Clock
        self.clock = Clock()

        #Idk man, some tile shit
        self.error_tile = pygame.image.load("sprites/tiles/unknown tile.png")


        # Game state
        self.gameOver = False
        self.isBetweenRounds = False
        self.roundIndex = 0
        self.round = self.settings.rounds[self.roundIndex].copy() # Deep copy not needed

        # Towers
        self.all_towers = []
        self.hoveringTower = None

        # Projectiles
        self.all_projectiles = []

        # Menu
        self.menu = Menu(self)
        self.health = 9
        self.money = 40
                
    def start_screen(self):
        self.start_menu = StartScreen(self.screen, self.gridIndex)
        while self.start_menu.wanted == True:
            
            self.input.update()
            self.start_menu.update_self(self.input.mouse)
            self._update_mouse()
            pygame.display.flip()
                    
        #Initialization of the game
        self.screen.fill([10,10,10])
        self.init_grid()
        self._start_grid()
            
            
#----------------------------------------------------------
#                        Functions
#----------------------------------------------------------

            
    def init_grid(self):
        #Grids
        self.grid = copy.deepcopy(self.settings.grids[self.gridIndex])
        self.entities_grid = copy.deepcopy(self.grid)

        #Pathfinding:
        self.path_finder = Path_finder(self.grid)

        path = self.path_finder.solve()
        if not path:
            raise errors.pathfinder_error

    

    def _start_grid(self):
        # This Places Tiles On The Grid, Based On The Number Given

        for row in range(len(self.grid)):
            for tile in range(len(self.grid[row])):
                position = self.grid[row][tile]
                #Position used for greater readability
                if position == 0:
                    position = Grass(self, tile, row)
                elif position == "P" or position == "B" or position == "E":  
                    position = Path(self, tile, row, self.path_finder.path)
                elif position == 2:
                    position = Scissor(self, tile, row)
                elif position == 3:
                    position = Knife(self, tile, row)

                self.grid[row][tile] = position

    def _update_screen(self):
        self._update_game_state()
        self._update_tiles()
        self._update_enemies()
        self._update_towers()
        self._update_projectiles()
        self._update_menu()
        self._update_mouse()

    def _update_game_state(self):
        # Add small break between rounds
        if self.isBetweenRounds: 
            if self.clock.get_time_since_last() > 10:
                self.clock.reset_lasttime()
                self.isBetweenRounds = False
        else:
            # Test if all rounds have been completed
            if self.health <= 0:
                self.gameOver = True
                return
            if len(self.round) == 0 and len(self.all_enemies) == 0: 
                if self.roundIndex + 1 >= len(self.settings.rounds):
                    self.gameOver = True
                    return
                self._next_round() # Start next round when game hasnt been completed
                self.isBetweenRounds = True
    
    def _update_menu(self):
        self.menu.update_self(self.money, self.health)


        # Check for buying towers
        if self.hoveringTower == None and self.input.mouse[2]:
            x = self.input.mouse[0]
            y = self.input.mouse[1]
            width = 80
            height = 80
            for button in self.menu.allTowerButtons:
                rectx = button.rect.x
                recty = button.rect.y
                if x >= rectx and y >= recty and x <= rectx+width and y <= recty+height:
                    self._buy_tower(button.towerName, button.cost)
        # Check for placing a tower that has been bought
        elif self.input.mouse[2]:
            if self.input.mouse[X] < 1240:
                x = self.input.mouse_grid_pos[X]
                y = self.input.mouse_grid_pos[Y]
                if self.entities_grid[y][x] == 0:
                    self._place_tower()


        


    def _update_tiles(self):
        for row in range(len(self.grid)):
            for tile in range(len(self.grid[row])):
                
                #In case that the tile is not a tile nor tower
                if not isinstance(self.grid[row][tile], Tile) and not isinstance(self.grid[row][tile], Tower):
                    rect = self.error_tile.get_rect()
                    self.screen.blit(self.error_tile, [tile*self.settings.tile_dim[X], row*self.settings.tile_dim[Y], self.settings.tile_dim[X], self.settings.tile_dim[Y]])
                else:
                    self.grid[row][tile].blit_self()

    def _update_mouse(self):
        if not self.hoveringTower == None:
            if self.hoveringTower == "scissor":
                image = pygame.image.load("sprites/towers/tower 2.png")
            elif self.hoveringTower == "knife":
                image = pygame.image.load("sprites/towers/box_cutter_tower_state_one.png")
            rect = image.get_rect()
            self.screen.blit(image, (self.input.mouse[0]-40, self.input.mouse[1]-40), rect)

        self.screen.blit(self.input.image, (self.input.mouse[0], self.input.mouse[1]), self.input.image.get_rect())

    def _update_enemies(self):

        # Dont spawn nor move enemies when between rounds
        if self.isBetweenRounds:
            return
        #----------------------------------------
        # From here, only updated every 0.6 seconds
        #----------------------------------------
        if self.clock.get_time_since_last() > 0.6: #Makes sure, that enemies only spawn and move every 0.6 seconds
            self.clock.reset_lasttime()
            # Move all enemies
            for enemy in self.all_enemies:
                enemy.move_enemy()

            # Remove all finished enemies from all_enemies list            
            if len(self.all_enemies) != 0: #Battles index error
                if self.all_enemies[0].hasFinished == True:
                    self.all_enemies.remove(enemy)
                    self.health -= enemy.damage

            # Update entity grid to make sure it reflects the current position of all enemies
            for coords in self.path_finder.path:
                self.entities_grid[coords[Y]][coords[X]] = "P"
            self.entities_grid[2][0] = "B"
            self.entities_grid[1][15] = "E"
            for enemy in self.all_enemies:
                self.entities_grid[enemy.pos[Y]][enemy.pos[X]] = enemy

        

            # Spawn new enemy
            self._spawn_enemy()

        #----------------------------------------
        # From here, updated every frame
        #----------------------------------------

        # Update all enemies and remove dead enemies
        for enemy in self.all_enemies:
            enemy.update_self()
            if not enemy.isAlive:
                self.all_enemies.remove(enemy)
                self.money += enemy.worth


    def _update_towers(self):
        for row in self.entities_grid:
            for tower in row:
                if isinstance(tower, Tower):
                    tower.update_self(self.entities_grid)
                    if tower.should_attack and not self.isBetweenRounds:
                        gridPos = tower.targetCoords
                        targetEnemy = self.entities_grid[gridPos[Y]][gridPos[X]]
                        spawnCoords = tower.gridPos
                        if isinstance(tower, Knife):
                            proj = KnifeArrow(spawnCoords, targetEnemy, self.path_finder.path, self)
                        elif isinstance(tower, Scissor):
                            proj = ScissorArrow(spawnCoords, targetEnemy, self.path_finder.path, self)
                        self.all_projectiles.append(proj)

    def _update_projectiles(self):
        for proj in self.all_projectiles:
            proj.update_self()
            if proj.done:
                self.all_projectiles.remove(proj)                  


    def _spawn_enemy(self):
        # Stop spawning enemies, when there is no more enmies left
        if len(self.round) == 0:
            return
        
        # Delete first enemy from list of enemies to spawn
        currentEnemy = self.round.pop(0)

        # Spawn before mentioned enemy
        if currentEnemy == 1:
            newEnemy = Papkasse(self.path_finder.path, self)
        elif currentEnemy == 2:
            newEnemy = Plastickasse(self.path_finder.path, self)
        else:
            return
        
        self.all_enemies.append(newEnemy)
        self.entities_grid[2][0] = newEnemy
            
    def _next_round(self):
        # Change to being between rounds and prepare next round
        self.isBetweenRounds = True
        self.roundIndex += 1
        if self.roundIndex == len(self.settings.rounds):
            self.round = []
            return
        self.round = copy.deepcopy(self.settings.rounds[self.roundIndex])
    
    def _buy_tower(self, towerName, cost):
        # Purchace tower if player has sufficient funds
        if cost <= self.money:
            self.money -= cost
            self.hoveringTower = towerName
    
    def _place_tower(self):
        # Place tower where mouse is positioned if tile is empty
        x = self.input.mouse_grid_pos[X]
        y = self.input.mouse_grid_pos[Y]
        if self.hoveringTower == "scissor":
            tower = Scissor(self, x, y)
        elif self.hoveringTower == "knife":
            tower = Knife(self, x, y)
        self.all_towers.append(tower)
        self.entities_grid[y][x] = tower
        self.hoveringTower = None

if __name__ == '__main__':
    for gridIndex in range(0,4):
        game = TD(gridIndex)
        game.start_screen()
        while not game.gameOver:
            game.input.update()
            game._update_screen()
            pygame.display.flip()
        if game.health < 0:
            break
