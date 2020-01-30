import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen, ai_settings):

        super(Ship,self).__init__()

        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('Images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerx-=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.ai_settings.ship_speed_factor

        if self.moving_up or self.moving_down:
            self.rect.centery=self.centery

        if self.moving_left or self.moving_right:
            self.rect.centerx=self.centerx


    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery=self.screen_rect.bottom
