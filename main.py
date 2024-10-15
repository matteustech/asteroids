import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0

    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        #player.draw(screen)
        #player.update(dt)
        
        for to_update in updatable:
            to_update.update(dt)

        for to_draw in drawable:
            to_draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

