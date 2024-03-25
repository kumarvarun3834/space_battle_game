import pygame, random,sys
from pygame.locals import *
import space_battle_data as data
from all_colours_fonts import *

def end_screen():
    end_screen_font = pygame.font.Font(None, 50)
    play_again_button = pygame.Rect(data.WIDTH // 2 - 100, 2 * data.HEIGHT // 3, 220, 50)  # Centered and adjusted button size

    play_again_text = end_screen_font.render("Play Again", True, BLACK)
    quit_button = pygame.Rect(data.WIDTH // 2 - 100, 2 * data.HEIGHT // 3 + 60, 220, 50)  # Centered and adjusted button position and size
    quit_text = end_screen_font.render("Main Menu", True, BLACK)
    text = end_screen_font.render(data.winner_text, True, BLACK)
    data.win.blit(text, (data.WIDTH // 2 - text.get_width() // 2, data.HEIGHT // 4))

    # Create "Play Again" button
    pygame.draw.rect(data.win, GREEN, play_again_button)
    data.win.blit(play_again_text, (play_again_button.x + (play_again_button.width - play_again_text.get_width()) // 2, play_again_button.y + 15))  # Center-aligned text

    # Create "Quit" button
    pygame.draw.rect(data.win, GREEN, quit_button)
    data.win.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + 15))  # Center-aligned text

    pygame.display.update()

    return play_again_button, quit_button
