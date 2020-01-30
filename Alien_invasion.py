import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from Alien import Alien

from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    stats=GameStats(ai_settings)
    ship=Ship(screen,ai_settings)
    bullets=Group()
    aliens=Group()
    play_button=Button(ai_settings,screen,"Play")
    sb=Scoreboard(ai_settings,screen,stats)


    bullet_sound = pygame.mixer.Sound('Music/bullet_new.wav')
    bullet_sound.set_volume(0.1)
    die = pygame.mixer.Sound('Music/game_over.wav')
    level = pygame.mixer.Sound('Music/level_completed.wav')
    level.set_volume(0.5)
    music = pygame.mixer.music.load('Music/music.mp3')
    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play(-1)

    gf.create_fleet(ai_settings,screen,ship,aliens,)
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens, bullets,bullet_sound)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,level)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets,die)

        gf.update_screen(ai_settings, screen,stats,sb, ship, aliens, bullets,play_button)








run_game()