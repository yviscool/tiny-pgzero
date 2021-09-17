import sys 
import time
import pygame

mod = sys.modules['__main__']

fps = 60
clock = pygame.time.Clock()

screen = None

def set_screen():
    global screen
    width = getattr(mod, 'WIDTH', 400)
    heigth = getattr(mod, 'HEIGHT', 400)
    screen = pygame.display.set_mode((width, heigth))
    mod.screen = screen

def go():

    set_screen()

    draw = mod.draw
    update = mod.update
    run = True

    while run:
        clock.tick(fps)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

