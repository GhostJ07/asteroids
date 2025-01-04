# this allows us to use code from
# the open-source pygame library
# throughout this file

# admin - Don't forget to activate your virtual env (see 'venv' in front of name)
# use command 'source venv/bin/activate' before running python 3

#pygame documentation: https://www.pygame.org/docs/ref/pygame.html

import pygame
from constants import *
from player import Player

def main():
    
    pygame.init(); #Initialising pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)); #setting the screen size of the 'window'
    clock = pygame.time.Clock() #creating a clock to make 60fps
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    
    while True : #creating an infinite game loop
        for event in pygame.event.get(): #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
        player.update(dt) #make the player rotate


        screen.fill("black") #filling that window in black
        player.draw(screen) #add tje player on the screen
        pygame.display.flip() #Use pygame's display.flip() method to refresh the screen. Be sure to call this last!

        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()