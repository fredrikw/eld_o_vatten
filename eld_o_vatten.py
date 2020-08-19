import sys
import pygame
import pygame.locals

pygame.init()

FramePerSec = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60
ACC = 0.5
FRIC = -0.12

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Eld och vatten')


class MyVec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return MyVec(newx, newy)

    def int_tuple(self):
        return (int(self.x), int(self.y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 30, 30))
        self.rect = self.surf.get_rect()
        self.pos = MyVec(50, 385)
        self.vel = MyVec(0, 0)
        self.acc = MyVec(0, 0)

    def run(self):
        self.acc = MyVec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.locals.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.locals.K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel

        self.pos.x = min(self.pos.x, WIDTH)
        self.pos.x = max(self.pos.x, 0)

        self.rect.midbottom = self.pos.int_tuple()


eldpojke = Player()

all_sprites = pygame.sprite.Group((eldpojke))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    eldpojke.run()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)
