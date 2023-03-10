class Settings:
    '''A class to store all settings for alien invasion'''

    def __init__(self):
        '''Initialize the game's static settings.'''
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (200, 200, 200)

        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15

        # Aniel settings. 
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5

        # How quickly the game speeds up.
        self.speed_up_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game.'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.7

        # fleet_direction of 1 represent right and -1 represent left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)