import sys
import pygame
import pygame.locals

pygame.init()

FramePerSec = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60
ACC = 0.5
FRIC = -0.12
GRAV = 0.5
JUMPSPEED = -10

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


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 15))
        self.surf.fill((30, 255, 30))
        self.rect = self.surf.get_rect(bottomleft=(0, HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 30, 30))
        self.rect = self.surf.get_rect()
        self.pos = MyVec(50, 385)
        self.vel = MyVec(0, 0)
        self.acc = MyVec(0, 0)

    def control(self):
        self.acc = MyVec(0, GRAV)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.locals.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.locals.K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[pygame.locals.K_UP]:
            self.jump()
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel

        self.pos.x = min(self.pos.x, WIDTH)
        self.pos.x = max(self.pos.x, 0)

        self.rect.midbottom = self.pos.int_tuple()

    def jump(self):
        if pygame.sprite.spritecollide(self, platforms, False):
            self.vel.y = JUMPSPEED

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0


eldpojke = Player()
mark = Platform()

all_sprites = pygame.sprite.Group((eldpojke, mark))
platforms = pygame.sprite.Group((mark,))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    eldpojke.control()
    eldpojke.update(platforms)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)
