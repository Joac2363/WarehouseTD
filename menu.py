import pygame
import colorsys


class Menu():
    def __init__(self, game):
        self.background = pygame.image.load("sprites/menu/menu_base.png")
        self.backgroundRect = self.background.get_rect()
        self.backgroundRect.x = 1280
        self.backgroundRect.y = 0
        self.screen = game.screen
        self.font = pygame.font.Font("fonts/ComicSansMS3.ttf", 60)
        self.image = pygame.image.load("sprites/menu/currency_icon.png")
        self.imageRect = self.image.get_rect()
        self.imageRect.centerx = 1600
        self.imageRect.y = 1
        self.allTowerButtons = [
            TowerButton(self.screen, "sprites/towers/tower 2.png",
                        15, [1400, 350], "scissor"),
            TowerButton(
                self.screen, "sprites/towers/box_cutter_tower_state_one.png", 25, [1680, 350], "knife")
        ]

    def update_self(self, money, health):
        self.screen.blit(self.background, self.backgroundRect)
        for button in self.allTowerButtons:
            button.blit_self()
        self._stats_update(money, health)
        self.screen.blit(self.image, self.imageRect)

    def _stats_update(self, money, health):
        moneyText = self.font.render(str(money), True, "black")
        moneyTextRect = moneyText.get_rect()
        moneyTextRect.center = [1600, 110]
        self.screen.blit(moneyText, moneyTextRect)

        if health >= 0 and health <= 10:
            image = pygame.image.load(
                f"sprites/menu/Health_bar/health_{10-health}.png")
        else:
            return
        rect = image.get_rect()
        rect.center = [1600, 185]
        self.screen.blit(image, rect)


class TowerButton():
    def __init__(self, screen, imagePath, cost, position, towerName):
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.screen = screen
        self.font = pygame.font.Font("fonts/ComicSansMS3.ttf", 30)
        self.price = self.font.render(str(cost), True, "black")
        self.priceRect = self.price.get_rect()
        self.priceRect.center = [position[0]+40, position[1]+170]

        self.cost = cost
        self.towerName = towerName

    def blit_self(self):
        self.screen.blit(self.price, self.priceRect)
        self.screen.blit(self.image, self.rect)
        
        
class MenuButton():
    def __init__(self, screen, start_pos: list, width_height: list, text: str, color: list, color_clicked: list, override_auto_font = 0):
        self.clicked = False
        self.highlighted = False
        self.screen = screen 
        self.text = text
        self.colors = [color, color_clicked]
        self.highlighted_color = self._dim_color(20)
        self.rect = pygame.Rect(start_pos[0], start_pos[1], width_height[0], width_height[1])

        if override_auto_font == 0:
            self.font = pygame.font.Font("fonts/ComicSansMS3.ttf", 1)
            self.font = self._calculate_font_size(self.font)
        else:
            self.font = pygame.font.Font("fonts/ComicSansMS3.ttf", override_auto_font)
        
        

    def update_self(self, mouse):
        self._check_clicked(mouse)
        self._draw_rect()
        self._draw_text()

    
    def _calculate_font_size(self, font):
        # Basically tries every single size one by one till it finds one that fits perfectly
        size = 1
        text_surface = self.font.render(self.text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        
        while text_rect.width < self.rect[2] and text_rect.height < self.rect[3]:
            size += 1
            font = pygame.font.Font("fonts/ComicSansMS3.ttf", size)
            text_surface = font.render(self.text, True, (0,0,0))
            text_rect = text_surface.get_rect()
            
        return pygame.font.Font("fonts/ComicSansMS3.ttf", size - 1)

    
    
    def _check_clicked(self, mouse: list):
        if (
            self.rect[0] <= mouse[0] <= self.rect[0] + self.rect[2] and
            self.rect[1] <= mouse[1] <= self.rect[1] + self.rect[3]
        ):
            self.highlighted = True
            self.clicked = mouse[2]
        else:
            self.highlighted = False
            self.clicked = False
    
    
    def _dim_color(self, dim_pct):
        #Dims the input color
        #Converts it to HSL (Hue Saturation Lightness, and times Lightness by 1 - the percentage)
        color = [int(c/255) for c in self.colors[0]]
        r, g, b = color
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        dimmed_brigthness = l * (1 - dim_pct/100)
        
        #Converts back to rgb
        dimmed_rgb = colorsys.hls_to_rgb(h, dimmed_brigthness, s)
        dimmed_rgb_int = [int(c * 255) for c in dimmed_rgb] 
        return dimmed_rgb_int

    
    
    
    def _draw_rect(self):
    
        if self.clicked:
            pygame.draw.rect(self.screen, self.colors[1], self.rect)
        
        elif self.highlighted:
            pygame.draw.rect(self.screen, self.highlighted_color, self.rect)
            
        else:
            pygame.draw.rect(self.screen, self.colors[0], self.rect)


    def _draw_text(self):

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        self.screen.blit(text_surface, text_rect)
        
        
class StartScreen():
    def __init__(self, screen, level):
        self.wanted = True
        self.screen = screen
        self.level = level
        self.background_img = pygame.image.load("sprites/menu/start_screen.png")
        self.text = "Tower Defense V - 0.2"
        self.font = pygame.font.Font("fonts/ComicSansMS3.ttf", 120)
        
        self.buttons = [
            MenuButton(self.screen, [560,630], [800, 200], "Start Game", [255, 55, 20], [0,0,0])
        ]


    def update_self(self, mouse):
        self._update_background()
        self._update_text()
        self._update_buttons(mouse)

        
        
    def _update_background(self):
        self.screen.blit(self.background_img, [0,0])
    
    def _update_buttons(self, mouse):
        for button in self.buttons:
            button.update_self(mouse)
        if self.buttons[0].clicked == True:
            self.wanted = False
        
    def _update_text(self):
        rect = pygame.Rect(0, 219, 1920, 410)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = rect.center)
        self.screen.blit(text_surface, text_rect)

        levelText = self.font.render(f"Level: {self.level+1}", True, "white")
        levelTextRect = levelText.get_rect()
        levelTextRect.center = [960,560]
        self.screen.blit(levelText, levelTextRect)
