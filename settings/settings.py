class Settings():
    """公共设置存储类"""
    def __init__(self):
        # 屏幕宽度
        self.screen_width = 1200
        # 屏幕高度
        self.screen_height = 800
        # 背景色
        self.bg_color = (0, 128, 128)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        # 飞船移动速度
        self.ship_speed_factor = 3
