import sys
import pygame

pygame.init()

FramePerSec = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 640, 480
FPS = 60

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Eld och vatten')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 30, 30))
        self.rect = self.surf.get_rect(center=(50, 420))


eldpojke = Player()

all_sprites = pygame.sprite.Group((eldpojke))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)
