from pygame import*

sswindow = display.set_mode((450,450))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("Backgroud.png"),(450,450))

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
    def P1_update(self):
        if key.get_pressed()[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key.get_pressed()[K_DOWN] and self.rect.y < 450 - 105:
            self.rect.y += self.speed
    def P2_update(self):
            if key.get_pressed()[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if key.get_pressed()[K_s] and self.rect.y < 450 - 105:
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

speed_x = 6
speed_y = 6

Racket =Player("Mw.png",415,175,5)
Racket1 =Player("Mw.png",10,175,5)
Ball=Enemy("Ball.png",202,202,3)

while True:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Ball.rect.x > 405 or Ball.rect.x < 0 or sprite.collide_rect(Ball,Racket) or sprite.collide_rect(Ball,Racket1):
        speed_x *= -1 
    if Ball.rect.y < 0 or Ball.rect.y >= 405 :
        speed_y *= -1    
    if Ball.rect.x < 10 or Ball.rect.x >= 400:
        print("GAME OVER")
        break
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y
    Racket.P1_update()
    Racket.reset()
    Racket1.P2_update()
    Racket1.reset()
    Ball.update()
    Ball.reset()
    time.Clock().tick(60)
    display.update()