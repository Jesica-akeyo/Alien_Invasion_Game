class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the Game's static Settings."""
        # screen settings        
        self.screen_width = 1200
        self.screen_height = 760
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 1
        self.bullet_color = 50, 20, 30
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 5
        
        # Creating settings for fleet direction
        self.fleet_drop_speed = 10
        
        # Fleet direction of 1 rep right; -1 rep left
        self.fleet_direction = 2

        # How quick;y the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase:
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize setings that can change during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 represents right; -1 rep left
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Icrease speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        


        

