from pygame import *

window = display.set_mode((450,450))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("Backgroud.png"),(450,450))

game = True

clock = time.Clock()


win_wight = 450
win_height = 450

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (25,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
            self.rect.y += self.speed

class Enemy(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (45,45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

Racket =Player("Mw.png",415,175,5)
Racket1 =Player2("Mw.png",10,175,5)
Ball=Enemy("Ball.png",202,202,3)

speed_x = 3
speed_y = 3

while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if Ball.rect.x > 405 :
        speed_x *= -1

    if Ball.rect.x < 0 :
        speed_x *= -1

    if Ball.rect.y < 0 :
        speed_y *= -1
    
    if Ball.rect.y >= 405 :
        speed_y *= -1

    if sprite.collide_rect(Ball,Racket) or sprite.collide_rect(Ball,Racket1):
            speed_x *= -1
    if Ball.rect.x < 10:
        print("Player1 к сожалению вы проиграли =(")
        break
    if Ball.rect.x >= 400:
        print("Player2 к сожалению вы проиграли =(")
        break
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y
    Racket.update()
    Racket.reset()
    Racket1.update()
    Racket1.reset()
    Ball.update()
    Ball.reset()
    clock.tick(60)
    display.update()