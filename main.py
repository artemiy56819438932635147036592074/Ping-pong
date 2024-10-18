from pygame import *
print("h")

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("ping pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 136:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 136:
            self.rect.y += self.speed

background = transform.scale(image.load("background.jpg"), (win_width,win_height))

racket_l = Player("racket.png",25,win_height/2,5,39,136)
racked_r = Player("racket.png",win_width-50,win_height/2,5,39,136)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0,0))
        racket_l.reset()
        racket_l.update_l()
        racked_r.reset()
        racked_r.update_r()
    display.update()