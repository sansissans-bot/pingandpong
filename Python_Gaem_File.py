from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__ (self, char_img, x, y, width, height, speed):
        self.image = transform.scale(image.load(char_img),(width,height))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = speed
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
    def p_left(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed
    def p_right(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))  
display.set_caption('trust me this will rage you')
player_left = player("images.jpg", 0, 50, 30, 100, 1)
player_right = player("images.jpg", win_width -30, 50, 30, 100, 1)

ball = player("download.jpg", randint(250, 500), randint(1, 350), 50, 50, 1)

game = True
finish = False
FPS = 1000
time = time.Clock()
ball_speed_x = ball.speed
ball_speed_y = ball.speed
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:  
            game = False  
           
    if not finish:
        window.fill((255,255,255))
        player_left.p_left()
        player_right.p_right()
        player_left.update()
        player_right.update()
        ball.update()
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if sprite.collide_rect(ball, player_left):
            ball_speed_x = ball.speed
        if sprite.collide_rect(ball, player_right):
            ball_speed_x = -ball.speed
        if ball.rect.y > win_height-50:
            ball_speed_y = -ball.speed
        if ball.rect.y < 0:
            ball_speed_y = ball.speed
            

# if ball flies behind this paddle, display loss condition for player 1
        if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (200, 200))


# if ball flies behind this paddle, display loss condition for player 2
        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(lose2, (200, 200))
        display.update()
        time.tick(FPS)
        