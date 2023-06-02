from pygame import *
back = (200, 255, 255)
clock = pygame.time.Clock()
moving_right = False
moving_left = False
mw = pygame.display.set_mode((500, 500))
mw.fill(back)

DARK_BLUE = (0, 0, 100)
LIGHT_RED = (250, 128, 114)

racket_x = 200
racket_y = 330
speed_x = 3
speed_y = 3

game_over = False

class Area():
    def __init__(self,x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x,y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def collderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x, y, width, height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

ball = Picture("ball.png", 160, 200, 50, 50)
platform = Picture("platform.png", racket_x, racket_y, 100, 30)


start_x = 5
start_y = 5
count = 9
monsters = []

for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)

    for i in range(count):
        d = Picture("enemy.png",x, y, 50,50)
        monsters.append(d)
        x = x + 55
    count = count - 1

while not game_over:
    if ball.rect.y > 350:
        game_over = True
    
    

    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
    if moving_left:
        platform.rect.x -= 3
    if moving_right:
        platform.rect.x += 3

    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0:
        speed_y*= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    
    if ball.rect.colliderect(platform.rect):
        speed_y *= -1

    for monster in monsters:
        monster.draw()
        if monster.rect.colliderect(ball.rect):
            speed_y *= -1
            monsters.remove(monster)
            monster.fill()

   




    platform.draw()
    ball.draw()


    if ball.rect.y > 350 or len(monsters) == 0:
        monsters = list()
        picture = Picture("789899.png", 100, 100, 500, 500)
        picture.fill()
        picture.draw()
        game_over = True
        pygame.display.update()
        

    #if game_over == True:
       #win = Label(0, 0, 500, 500, LIGHT_GREEN)
       #win.set_text("Ты победил!!!", 60, DARK_BLUE)
       #win.draw(140, 180)
       #resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
       #resul_time.set_text("Время прохождения: " + str (int(new_time - start_time)) + " сек", 40, DARK_BLUE)
 
    pygame.display.update()
    clock.tick(40)
