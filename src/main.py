import pygame

def main():
    """ Main program """
    screenSize = (576, 1024)
    
    ## initializing game
    pygame.init()

    # creating the display window
    screen = pygame.display.set_mode(screenSize)

    # manages the frame rate 
    clock = pygame.time.Clock()

    while True:

        # loop that runs continuously as events occur
        for event in pygame.event.get():

            # allows for quitting the game through window exit button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        # limiting the frame rate
        clock.tick(120)

if __name__ == "__main__":
    main()