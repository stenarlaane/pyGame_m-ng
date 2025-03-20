import pygame

background_color = (100, 7, 163)
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Blaster!")

screen.fill(background_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
pygame.quit()