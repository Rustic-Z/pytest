import pygame
import game_functions as gf
from settings.settings import Settings
from role.ship import Ship
from role.alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.display.set_caption("打飞机")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船对象
    ship = Ship(ai_settings, screen)
    # 创建外星人对象
    alien = Alien(screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, alien)

run_game()
