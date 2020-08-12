class Settings:
    def __init__(self):
        self.screen_width =1000
        self.screen_height = 600
        self.bg_img = pygame.image.load("./img/bg_img.png")
        self.plane_speed = 2.5
class Plane:
    def __init__(self,screen):
        self.screen = screen
        self.img_plane = pygame.image.load()
        self.rect = self.img_plane.get_rect()
        self.screen_rect.cencerx = self.screen_rect.centerx
        self.rect.centerx = self.screen_rect.centerx # 水平居中
          

        self.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    标志位
          self.mv_right = False
          self.mv_left = False
      def update(self):
          
          # 根据标志位的调整小飞机的位置
          if self.mv_right:
              self.rect.centerx += 1
          if self.mv_right:
              self.rect.centerx += 1  
          if self.mv_left:
              self.rect.centerx += 1


    def blitme(self):
        self.screen.blit(self.img_plane,self.rect)