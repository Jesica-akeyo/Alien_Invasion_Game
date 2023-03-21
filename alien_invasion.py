import pygame
from pygame._sdl2 import Window, Renderer
from pygame.sprite import Group
from settings import Settings   
from game_stats import GameStatistics
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion by Jesica Brian and Samuel")

    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and make a scoreboard
    # Create an instance to store game settings
    stats = GameStatistics(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, group of bullets and group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    # Start the mwain loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
       
run_game()
   