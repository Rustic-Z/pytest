import pygame

class Alien():
    """外星人来啦"""
    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('imgs/alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        """外星人列队啦"""
        self.screen.blit(self.image, self.rect)
