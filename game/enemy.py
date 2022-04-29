import pygame
from bullet import bullet


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
twidth = 30

FPS = 30

endefaultspeed = 5
endefaultrectx = 100
endefaultrecty = 100
endefaulthealth = 5
endefaultdir = 'right'

enshootspeed = 15
bulgenl = 5

directions = ['left', 'right', 'up', 'down']

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'enemy'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((twidth, twidth))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = endefaultspeed
        self.oldx = endefaultrectx
        self.oldy = endefaultrecty
        self.rect.x = endefaultrectx
        self.rect.y = endefaultrecty
        self.direction = 'right'
        self.health = endefaulthealth
        self.cooldown = 0
        self.cooldown2 = 0

    def update(self):
        self.cooldown += 1
        if self.cooldown > FPS:
            if self.direction == 'right':
                self.direction = 'up'
            elif self.direction == 'up':
                self.direction = 'left'
            elif self.direction == 'left':
                self.direction = 'down'
            elif self.direction == 'down':
                self.direction = 'right'
            self.cooldown = 0
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

    def ishot(self, bullet):
        pass

    def die(self):
        pass

    def isalive(self):
        pass

    def shoot(self):
        if self.cooldown2 > enshootspeed:
            self.cooldown2 = 0
            a = bullet()
            a.direction = self.direction
            if self.direction == 'right':
                a.rect.x = self.rect.x + self.image.get_width() + bulgenl
                a.rect.y = self.rect.y + self.image.get_height() // 2
            elif self.direction == 'left':
                a.rect.x = self.rect.x - bulgenl
                a.rect.y = self.rect.y + self.image.get_height() // 2
            if self.direction == 'up':
                a.rect.x = self.rect.x + self.image.get_width() // 2
                a.rect.y = self.rect.y - bulgenl
            if self.direction == 'down':
                a.rect.x = self.rect.x + self.image.get_width() // 2
                a.rect.y = self.rect.y + self.image.get_height() + bulgenl
            return a
        else:
            self.cooldown2 += 1
            return None
