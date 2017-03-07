import sys
import pygame

def check_events(ship):
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship, alien):
    # 设置屏幕颜色
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
    # 让最近绘制电屏幕可见
    pygame.display.flip()
