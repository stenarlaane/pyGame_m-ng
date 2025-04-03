import pygame
from settings import Settings
from spritez import Player
from bubble import Bubble
import game_func as gf


pygame.init()
gm_set = Settings()
screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
pygame.display.set_caption(gm_set.caption)
running = True
player = Player(screen)
bubble = Bubble(screen, gm_set)
bubbles = pygame.sprite.Group()
while True:
    gf.check_events(gm_set, screen, player, bubbles)
    player.update()
    bubbles.update()
    gf.update_screen(gm_set, screen, player, bubbles)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(gm_set.bg_color)
    gf.check_events()
    pygame.display.flip()
pygame.quit()