import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavirs """

    def __init__(self):
        """Initialize the game and create game resources """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion by Jesica Brian and Samuel")

        #make a ship
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()

        # Set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.update()          
            self._update_screen()
            
    def _check_events(self):#helper method
        """Respond to key presses and mouse events"""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        #exit game easily    
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the group"""
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)

    def _update_screen(self):
         """Update images on the screen, and flip to the new screen"""
         # Redraw the screen during each pass through theloop
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         for bullet in self.bullet.sprites():
             bullet.draw_bullet()

         # Make the most recently drawn screen visible.
         pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()