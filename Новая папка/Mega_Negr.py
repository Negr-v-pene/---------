from pygame import *

window = display.set_mode((450,450))
display.set_caption("Negrylya")
background = transform.scale(image.load("Negrylya.png"),(450,450))

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

class Enemy():
    def __init__(self, player_image, player_x, player_y, player_speed, player_speed_y,player_speed_x):
        self.image = transform.scale(image.load(player_image), (45,45))
        self.speed = player_speed
        self.speed_x = player_speed_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        pass

hernya2=Player2("eldisha.png",415,175,5)
hernya1=Player("eldisha.png",10,175,5)
vzx=Enemy("vzx-removebg-preview.png",202,202,3,3,3)

while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    vzx.rect.x += 3
    hernya1.update()
    hernya1.reset()
    hernya2.update()
    hernya2.reset()
    vzx.update()
    vzx.reset()
    clock.tick(60)
    display.update()