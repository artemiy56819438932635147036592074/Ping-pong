from pygame import *
print("h")

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("ping pong")

clock = time.Clock()

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

racket_l = Player("racket.png",25,win_height/2,10,39,136)
racked_r = Player("racket.png",win_width-50,win_height/2,5,39,136)
ball = GameSprite("tenis_ball.png",win_width/2,win_height/2,10,50,50)

font.init()

font2 = font.SysFont("Arial",72)
Pl1_win = font2.render("PLAYER 2 LOSE",1,(255,0,0))
Pl2_win = font2.render("PLAYER 1 LOSE",1,(255,0,0))
reatart_label = font2.render("r-restart",1,(255,0,0))

ball_speedx = 5
ball_speedy = 5

def restart():
    finish = False
    ball.rect.x = win_width/2
    ball.rect.y = win_height/2

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                restart()

    
    if finish != True:
        ball.rect.x += ball_speedx
        ball.rect.y += ball_speedy
        window.blit(background,(0,0))
        ball.reset()
        racket_l.reset()
        racket_l.update_l()
        racked_r.reset()
        racked_r.update_r()
        if ball.rect.y <= 0:
            ball_speedy *= -1
        if ball.rect.y >= win_height-50:
            ball_speedy *= -1
        if sprite.collide_rect(ball,racket_l) or sprite.collide_rect(ball,racked_r):
            ball_speedx *= -1
        if ball.rect.x < 0:
            window.blit(Pl2_win,(100,win_height/2))
            window.blit(reatart_label,(150,(win_height/2)+ 50))
            finish = True
        if ball.rect.x > win_width:
            window.blit(Pl1_win,(100,win_height/2))
            window.blit(reatart_label,(150,(win_height/2)+50))
            finish = True

    display.update()
    clock.tick(40)