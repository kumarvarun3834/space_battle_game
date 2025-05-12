from all_colours_fonts import * 
import os
import pygame 
# Create a window to initialize the video system
pygame.display.init()
game_over = False
end_screen_displayed = False
speed=5
BULLET_SPEED=7
yellow_bullets=[]
red_bullets=[]
MAX_BULLET=5
YELLOW_HIT=pygame.USEREVENT+2
RED_HIT=pygame.USEREVENT+1
MAX_HEALTH=10
RED_HEALTH=MAX_HEALTH
YELLOW_HEALTH=MAX_HEALTH
#WIDTH,HEIGHT=900,500
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

border=(WIDTH//2-5,0,10,HEIGHT)
win=pygame.display.set_mode((WIDTH,HEIGHT))
# Define button dimensions
BUTTON_WIDTH = 220
BUTTON_HEIGHT = 60
BUTTON_COLOR=BLUE
BUTTON_HOVER_COLOR=RED
play_again_button = None
quit_button = None
pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 80)
WINNER_FONT=pygame.font.SysFont("comicsans",200)

def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'Assets/', filename)

pygame.mixer.init()
bullet_hit_sound=pygame.mixer.Sound(get_asset_path("Grenade+1.mp3"))
bullet_fire_sound=pygame.mixer.Sound(get_asset_path('Gun+Silencer.mp3'))
jet=pygame.mixer.Sound(get_asset_path("good-jetpack-sound-loop-96693.mp3"))
title=get_asset_path("the_field_of_dreams.mp3")
SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT=120,120
RED_SHIP_image=pygame.image.load(get_asset_path("white_ship.png"))
RED_SHIP=pygame.transform.rotate(pygame.transform.scale(RED_SHIP_image,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),90)
YELLOW_SHIP_image=pygame.image.load(get_asset_path("blue_ship.png"))
YELLOW_SHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP_image,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),-90)
space=pygame.transform.scale(pygame.image.load(get_asset_path("space.png")),(WIDTH,HEIGHT))

logo=pygame.transform.scale(pygame.image.load(get_asset_path("BattleSpaceHomeScreen.png")),(WIDTH,HEIGHT))
