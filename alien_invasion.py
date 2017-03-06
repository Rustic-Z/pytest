import sys
import pygame
from settings.settings import Settings
from role.ship import Ship
from role.alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.display.set_caption("打飞机")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 创建飞船对象
    ship = Ship(screen)
    # 创建外星人对象
    alien = Alien(screen)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 设置屏幕颜色
        screen.fill(ai_settings.bg_color)

        ship.blitme()
        alien.blitme()

        # 让最近绘制电屏幕可见
        pygame.display.flip()

run_game()
