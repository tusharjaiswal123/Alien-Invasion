
class Settings():
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_limit=3

        self.bullet_width=5
        self.bullet_height=25
        self.bullet_color=60,60,60
        self.bullets_allowed=8

        self.fleet_drop_speed=35

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # 1 for right and -1 for left

        self.alien_points=50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)