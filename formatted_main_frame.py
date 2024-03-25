import pygame,math,random,time
from pygame.locals import *
from all_colours_fonts import *
import space_battle_data as data

def logo_window():
    data.win.blit(data.logo,(0,0))
    LOGO_other_elements()
    # Create a function to draw buttons
    def draw_button(x, y, text, action):
        button_rect = pygame.Rect(x, y, data.BUTTON_WIDTH, data.BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(data.win, data.BUTTON_HOVER_COLOR, button_rect)
            if click[0] == 1:
                if action == "start":
                    # Added code to start the game
                    start_game()

                elif action == "about":
                    # Add code to show about information gemeral_main_frameproduced and all
                    show_about()

                elif action == "quit":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(data.win, data.BUTTON_COLOR, button_rect)

        # Render button text
        text_surface = MAIN_FRAME_FONT.render(text, True,BLACK)
        text_rect = text_surface.get_rect(center=(x + data.BUTTON_WIDTH // 2, y + data.BUTTON_HEIGHT // 2))
        data.win.blit(text_surface, text_rect)

    # Draw buttons
    draw_button(400,300 , "Start", "start")
    draw_button(400,350 , "About", "about")
    draw_button(400,400 , "Quit", "quit")
    pygame.display.update()

def LOGO_other_elements():
    pass

def start_game():
    print("start button working")
    import space_battle as main_game
    data.YELLOW_HEALTH,data.RED_HEALTH=data.MAX_HEALTH,data.MAX_HEALTH
    main_game.space_shooting_main()
    # Add code to initialize and start your game

def show_about():
    print("about button working")
    # AboutSection(data.win)
    # Add code to display information about the game
    pass

def main_frame_setup():
    pygame.init()
    pygame.display.set_caption("SPACE BATTLE")
    pygame.mixer.music.load(data.title)
    pygame.mixer.music.play()
    FPS = 40
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                QUIT()

        data.win.fill((0, 0, 0))  # Clear the screeN
        
        logo_window()
        pygame.display.update()
        clock.tick(FPS)

main_frame_setup()