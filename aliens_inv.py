import sys

import pygame

def run_game():
    #Game screen up and created
    pygame.init() # initialize the background pygame need to run properly
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Aliens duh")

    #Set Back color
    bg_color = (230, 230 ,230)

#Start of the loop
    while True:

        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen during each pass through the loop
        screen.fill(bg_color)

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()