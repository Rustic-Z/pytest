import pygame

class Ship():
    """英雄,飞船开走打怪兽吧～"""
    def __init__(self, screen):
        """飞机上炮加油"""
        super(Ship, self).__init__()
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('imgs/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
