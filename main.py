# this allows us to use code from
# the open-source pygame library
# throughout this file

# admin - Don't forget to activate your virtual env (see 'venv' in front of name)
# use command 'source venv/bin/activate' before running python 3

#pygame documentation: https://www.pygame.org/docs/ref/pygame.html

import pygame
from constants import *

def main():
    
    pygame.init(); #Initialising pygame

    print ("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)); #setting the screen size of the 'window'

    while True : #creating an infinite game loop
        for event in pygame.event.get(): #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") #filling that window in black
        pygame.display.flip() #Use pygame's display.flip() method to refresh the screen. Be sure to call this last!
        
    
    
if __name__ == "__main__":
    main()