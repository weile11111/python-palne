import pygame
from settings import Settings
from plane import Plane
import game_func as fg
from spaceship import Spaceship
from pygame.sprite import Group


def run_game():

    # 初始化游戏

    pygame.init()

    # 设置屏幕分辨率

    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("飞机大战")
    

    # 创建小飞机
    plane = Plane(screen,setting)
    # print(bg_img)
    spaceship = Spaceship(setting,screen)
    # 开始游戏的主循环
    while True:

       # 不关闭窗口
       
       fg.check_events()

       # 绘制图像

       fg.update_screen(screen,setting.bg_img,plane)

run_game()

     


              




