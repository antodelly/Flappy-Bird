import pygame
import random
import os

def draw_items():
    screen.blit(background, (0, 0))
    screen.blit(bird, (bird_x, bird_y))

def refrash():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'immagini') # The image folder path

screen = pygame.display.set_mode([288, 512])
pygame.display.set_caption('Flappy Bird')
background = pygame.image.load(os.path.join(image_path, 'sfondo.png'))
bird = pygame.image.load(os.path.join(image_path, 'uccello.png'))
base = pygame.image.load(os.path.join(image_path, 'base.png'))
gameover = pygame.image.load(os.path.join(image_path, 'gameover.png'))
downtube = pygame.image.load(os.path.join(image_path, 'tubo.png'))
uppertube = pygame.transform.flip(downtube, False, True)
pygame.display.set_icon(bird)
fps = 60
bird_x, bird_y, bird_run_y = 60, 150, 0

# Run until the user asks to quit
running = True
while running:
    bird_run_y += 1
    bird_y += bird_run_y
    draw_items()
    refrash()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Done! Time to quit.
pygame.quit()
    
