class Settings:
    """ A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
<<<<<<< HEAD
        
        #Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right and -1 represents left
        self.fleet_direction = 1
        
=======

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represents right and -1 rep left
        self.fleet_direction = 1
>>>>>>> e98ce4e67f44118ef36207b9b8d1d01ce45b1ffe
