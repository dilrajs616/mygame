class Settings:
    '''A class to store all settings for alien invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (200, 200, 200)

        # Ship settings
        self.ship_speed = 1

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aniel settings. 
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 repressents right; -1 represents left.
        self.fleet_direction = 1