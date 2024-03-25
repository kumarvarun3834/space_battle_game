import pygame
from pygame.locals import *
import space_battle_data as data
from all_colours_fonts import *
class Border:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
top_border = Border(0, 0, data.WIDTH, 10)
bottom_border = Border(0, data.HEIGHT - 10, data.WIDTH, 10)
left_border = Border(0, 0, 10, data.HEIGHT)
right_border = Border(data.WIDTH - 10, 0, 10, data.HEIGHT)

# Create a vertical center border
center_border = Border(data.WIDTH // 2 - 5, 0, 10, data.HEIGHT)


# game window
def draw_window(red,yellow,RED_HEALTH,YELLOW_HEALTH):
    data.win.blit(data.space,(0,0))
    # data.win.fill(WHITE)
    data.win.blit(data.YELLOW_SHIP,(yellow.x,yellow.y))
    data.win.blit(data.RED_SHIP,(red.x,red.y))
    RED_HEALTH_TEXT=HEALTH_FONT.render("health: "+str(RED_HEALTH),1,WHITE)
    YELLOW_HEALTH_TEXT=HEALTH_FONT.render("health: "+str(YELLOW_HEALTH),1,WHITE)
    data.win.blit(RED_HEALTH_TEXT,(data.WIDTH-RED_HEALTH_TEXT.get_width()-10,10))
    data.win.blit(YELLOW_HEALTH_TEXT,(10,10))


    pygame.display.update()

def HANDLE_BULLETS(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += data.BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(data.RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x>data.WIDTH:
            yellow_bullets.remove(bullet)
        pygame.draw.rect(data.win, YELLOW, bullet)

    for bullet in data.red_bullets:
        bullet.x -= data.BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(data.YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)
        pygame.draw.rect(data.win, RED, bullet)
    pygame.display.update()

def ship_yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - data.speed > 0: # left
        yellow.x-=data.speed
        data.jet.play()
    if key_pressed[pygame.K_d] and yellow.x + data.speed + yellow.width < center_border.x: # right
        yellow.x+=data.speed
        data.jet.play()
    if key_pressed[pygame.K_w] and yellow.y > 0: # up
        yellow.y-=data.speed
        data.jet.play()
    if key_pressed[pygame.K_s]and yellow.y + data.speed + yellow.height < data.HEIGHT-10: # down
        yellow.y+=data.speed
        data.jet.play()

def ship_red_movement(key_pressed,red):
    if key_pressed[pygame.K_j] and red.x - data.speed > 470:  # left
        red.x -= data.speed
        data.jet.play()
    if key_pressed[pygame.K_l] and red.x + data.speed < 900-red.width+10:  # right
        red.x += data.speed
        data.jet.play()
    if key_pressed[pygame.K_i] and red.y > 0:  # up
        red.y -= data.speed
        data.jet.play()
    if key_pressed[pygame.K_k] and red.y + data.speed + red.height < data.HEIGHT - top_border.height:  # down
        red.y += data.speed
        data.jet.play()

def firing(key_pressed,yellow,red):
    if key_pressed[K_LCTRL]:
        if len(data.yellow_bullets)<=data.MAX_BULLET:
            bullet= pygame.Rect(data.yellow.x+data.yellow.width-40,data.yellow.y+30,20,3)
            data.yellow_bullets.append(bullet)
            data.bullet_fire_sound.play()

    if key_pressed[K_RCTRL]:
        if len(data.red_bullets)<=data.MAX_BULLET:
            bullet= pygame.Rect(data.red.x+10,data.red.y+30,20,3)
            data.red_bullets.append(bullet)
            data.bullet_fire_sound.play()

            # Red ship is firing
            # Implement firing logic for the data.red ship here

def DRAW_WINNER(TEXT):
    TEXT_TEMP=WINNER_FONT.render(TEXT,1,WHITE)
    data.win.blit(TEXT_TEMP,(data.WIDTH/2-TEXT_TEMP.get_width()/2,10))
    pygame.display.update()

def space_shooting_main():
    global RED_HEALTH,YELLOW_HEALTH
    data.red=pygame.Rect(700,250,data.SPACE_SHIP_WIDTH,data.SPACE_SHIP_HEIGHT)
    data.yellow=pygame.Rect(100,250,data.SPACE_SHIP_WIDTH,data.SPACE_SHIP_HEIGHT)

    pygame.init()
    pygame.display.set_caption("SPACE FIGHTING GAME")
    # display of game
    FPS = 40
    #set the FPS of game at which it runs
    clock= pygame.time.Clock()
    # draw_window(data.red,data.yellow)    
    pygame.display.update()
    run=True
    while run:
        clock.tick(FPS)
        if data.game_over ==False and data.end_screen_displayed==False:
            draw_window(data.red,data.yellow,data.RED_HEALTH,data.YELLOW_HEALTH)
        for event in pygame.event.get():
            # first get about quitting statement
            if event.type == pygame.QUIT:
                run=False  
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                print(x,y)
            key_pressed=pygame.key.get_pressed()
            if data.game_over ==False and data.end_screen_displayed==False:
                ship_yellow_movement(key_pressed,data.yellow)
                ship_red_movement(key_pressed,data.red)             
                firing(key_pressed,data.yellow,data.red)
            if event.type==data.RED_HIT:
                data.RED_HEALTH-=1
                data.bullet_hit_sound.play()
            if event.type==data.YELLOW_HIT:
                data.YELLOW_HEALTH-=1
            data.bullet_hit_sound.play()
            if data.YELLOW_HEALTH<=0 or data.RED_HEALTH <=0:
                data.game_over = True
                data.end_screen_displayed = True
        
        HANDLE_BULLETS(data.yellow_bullets,data.red_bullets,data.yellow,data.red)
            # Move and draw bullets
        
        if data.RED_HEALTH<=0:
            data.winner_text="yellow player won the game!"
            # space_battle_end_screen.winner_text()
        elif data.YELLOW_HEALTH<=0:
            data.winner_text="yellow player won the game!"
            # space_battle_end_screen.winner_text()
            
        if data.game_over and data.end_screen_displayed:
            import space_battle_end_screen as space_battle_end_screen
            play_again_button, quit_button = space_battle_end_screen.end_screen()

            # Handle the buttons only when the game is over and the end screen is displayed
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if play_again_button.collidepoint(m_x, m_y):
                        data.game_over = False
                        data.end_screen_displayed = False
                        data.RED_HEALTH,data.YELLOW_HEALTH=data.MAX_HEALTH,data.MAX_HEALTH
                    elif quit_button.collidepoint(m_x, m_y):
                        import formatted_main_frame
                        formatted_main_frame.main_frame_setup()
# space_shooting_main()   
            
