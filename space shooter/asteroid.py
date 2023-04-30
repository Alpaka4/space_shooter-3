from settings import *
import pygame
import random
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,screen,image_list):
        image_original = random.choice(image_list)
        image_original.set_colorkey(BLACK)
        self.image = image_original.copy()
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.8 / 2
        self.rect.bottom = random.randint(-80,0)
        self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
        self.speedy= random.randint(1,5)
        self.speedx= random.randint(-2,2)
        self.damage = 0
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.right<LEFT_BORDER:
            self.rect.bottom = random.randint(-80,0)
            self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
        if self.rect.left>RIGHT_BORDER:
            self.rect.bottom = random.randint(-80,0)
            self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
    def draw(self):
        self.screen.blit(self.image, self.rect)
