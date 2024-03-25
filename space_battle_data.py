
from all_colours_fonts import * 
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
WIDTH,HEIGHT=900,500
border=(WIDTH//2-5,0,10,HEIGHT)
win=pygame.display.set_mode((WIDTH,HEIGHT))
# Define button dimensions
BUTTON_WIDTH = 110
BUTTON_HEIGHT = 30
BUTTON_COLOR=BLUE
BUTTON_HOVER_COLOR=RED
play_again_button = None
quit_button = None
pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT=pygame.font.SysFont("comicsans",100)

pygame.mixer.init()
bullet_hit_sound=pygame.mixer.Sound("pygames/space_battle/Assets/Grenade+1.mp3")
bullet_fire_sound=pygame.mixer.Sound('pygames/space_battle/Assets/Gun+Silencer.mp3')
jet=pygame.mixer.Sound("pygames/space_battle/Assets/good-jetpack-sound-loop-96693.mp3")
title="pygames/space_battle/Assets/the_field_of_dreams.mp3"
SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT=60,60
RED_SHIP_image=pygame.image.load("pygames/space_battle/Assets/white_ship.png")
RED_SHIP=pygame.transform.rotate(pygame.transform.scale(RED_SHIP_image,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),90)
YELLOW_SHIP_image=pygame.image.load("pygames/space_battle/Assets/blue_ship.png")
YELLOW_SHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP_image,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),-90)
space=pygame.transform.scale(pygame.image.load("pygames/space_battle/Assets/space.png"),(WIDTH,HEIGHT))

logo=pygame.transform.scale(pygame.image.load("pygames/space_battle/Assets/BattleSpaceHomeScreen.png"),(WIDTH,HEIGHT))
