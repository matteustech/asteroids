import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for asteroid in asteroids:
            if asteroid.collidesWith(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collidesWith(shot):
                    asteroid.split()
                    asteroid.kill()
                    break


        for to_update in updatable:
            to_update.update(dt)

        for to_draw in drawable:
            to_draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

