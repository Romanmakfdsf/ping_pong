from pygame import * 
from random import *
#подключение музыки


font.init()
font = font.SysFont('Arial', 45)
win1 = font.render('LEFT PLAYER WINS!', True, (40,0,0))
win2 = font.render('RIGHT PLAYER WINS!', True, (40,0,0))
#название музыки
img_back = "fon.jpg"
img_board = "board.png" 
img_ball = "ballon.png" 

ball_x = 160
ball_y = 200
speed_x = 1
speed_y = 1
clock = time.Clock()
# создание класса GameSprite
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, direction):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.direction = direction
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 

# создание корабля - класс наследник GameSprite
class Player1(GameSprite):
   def update_right(self):
       keys = key.get_pressed()
       if keys[K_DOWN] and self.rect.y < 480:
           self.rect.y += self.speed
       if keys[K_UP] and self.rect.y < 480:
           self.rect.y -= self.speed

   def update_left(self):
       keys = key.get_pressed()
       if keys[K_s] and self.rect.y < 480:
           self.rect.y += self.speed
       if keys[K_w] and self.rect.y < 480:
           self.rect.y -= self.speed
        
class Ball(GameSprite):
    def update(self):
        if self.direction == 1:
            self.rect.x += 3
            self.rect.y -= 3
        elif self.direction == 4:
            self.rect.x -= 3
            self.rect.y -= 3
        elif self.direction == 3:
            self.rect.x -= 3
            self.rect.y += 3
        elif self.direction == 2:
            self.rect.x += 3
            self.rect.y += 3
        if self.rect.y < 0:
            if self.direction == 1:
                self.direction = 2
            elif self.direction == 4:
                self.direction = 3
        if self.rect.y > 450:
            if self.direction == 2:
                self.direction = 1
            elif self.direction == 3:
                self.direction = 4
            
 
 


  


 
 

win_width = 500 # ширина окна
win_height = 500 # высота окна
display.set_caption("Ping_pong") # название окна
window = display.set_mode((win_width, win_height)) # создание окна
background = transform.scale(image.load(img_back), (win_width, win_height)) # установка картинки заднего фона
 

board1 = Player1(img_board, 40, win_height - 280, 40, 80, 10,0)
board2 = Player1(img_board, 420, win_height - 280, 40, 80, 10,0)
ball = Ball(img_ball, 230, 250, 50, 50, None, randint(1,4))

 
 
 
 

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
          
 
 
    if not finish: # если игра не закончена

        window.blit(background,(0,0)) # поставить фон в окно
        if ball.rect.x > 500:
            window.blit(win1, (60, 200))
            finish = True
        if ball.rect.x < 0:
            window.blit(win2, (60, 200))
            finish = True

        board1.update_left()
        board2.update_right()
        ball.update()
        board1.reset()
        board2.reset()
        ball.reset()
        if sprite.collide_rect(ball, board1):
            if ball.direction == 4:
                ball.direction = 1
            elif ball.direction == 3:
                ball.direction = 2
        if sprite.collide_rect(ball, board2):
            if ball.direction == 2:
                ball.direction = 3
            elif ball.direction == 1:
                ball.direction = 4
      
        
 
        display.update()
    clock.tick(60)