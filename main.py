# this allows us to use code from
# the open-source pygame library
# throughout this file

# admin - Don't forget to activate your virtual env (see 'venv' in front of name)
# use command 'source venv/bin/activate' before running python 3

#pygame documentation: https://www.pygame.org/docs/ref/pygame.html

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    
    pygame.init(); #Initialising pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)); #setting the screen size of the 'window'
    clock = pygame.time.Clock() #creating a clock to make 60fps

    updatable = pygame.sprite.Group() #create the groupes first before allocating them
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #Note: After changing a static field like containers, make sure to create all Player objects after the change. This way, they will be correctly added to the groups.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0
    
    while True : #creating an infinite game loop
        for event in pygame.event.get(): #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return

        for obj in updatable:    
            obj.update(dt)   #make the player rotate, move, spawn astroids,

        for asteroid in asteroids:  #check if there is collision with player
            if player.collision(asteroid):
                print("Game over!")
                sys.exit() #exit the game immediatly

        screen.fill("black") #filling that window in black
        for obj in drawable:
            obj.draw(screen) #add the player on the screen
        pygame.display.flip() #Use pygame's display.flip() method to refresh the screen. Be sure to call this last!

        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()