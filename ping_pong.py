from pygame import *

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height- 100 :
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height- 100:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed

win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load('sky.jpg'), (win_width, win_height))

player_l = Player('racket.png', 8,200,50,100, 6)
player_r = Player('racket.png', 738,20,50,100,6)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 10)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

game =True
clock = time.Clock()
FPS = 60
finish = False

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    

    if finish != True:
        window.blit(background,(0, 0))
        
        player_l.reset()
        player_l.update_l()

        player_r.reset()
        player_r.update_r()

        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_l,ball) or sprite.collide_rect(player_r,ball):
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))


    display.update()
    clock.tick(FPS)
