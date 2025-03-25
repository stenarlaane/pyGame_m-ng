import pygame
from settings import Settings
from spritez import Player
import game_func as gf


pygame.init()
gm_set = Settings()
screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
pygame.display.set_caption(gm_set.caption)
running = True
player = Player(screen)
while True:
    gf.check_events(player)
    player.update()
    gf.update_screen(gm_set, screen, player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(gm_set.bg_color)
    gf.check_events()
    player.blit_me()
    pygame.display.flip()
pygame.quit()