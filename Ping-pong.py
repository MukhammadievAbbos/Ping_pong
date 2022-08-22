from random import randint
from time import time as timer
from re import M

from pygame import *

window = display.set_mode((800, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('background1.jpg'), (800, 500))


mixer.init()

mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Verdana', 40)
lost = 0
kills = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.direction = ' '

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class PLayer(GameSprite):
    def update(self):
        keys = key.get_pressed()
        pass


racket1 = PLayer('racket.png', 30, 200, 50, 150, 10)
racket2 = PLayer('racket.png', 30, 200, 50, 150, 10)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 5)

game = True
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick()
