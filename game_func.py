import pygame
import sys
from bubble import Bubble


pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)


def check_events(gm_set, screen, player, bubbles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDBUBBLE:
            create_bubble(gm_set, screen, bubbles)


def create_bubble(gm_set, screen, bubbles):
    new_bubble = Bubble(screen, gm_set)
    bubbles.add(new_bubble)


def update_bubbles(player, bubbles):
    hitted_bubble = pygame.sprite.spritecollideany(player, bubbles)
    if hitted_bubble != None:
        hitted_bubble.kill()


def update_screen(gm_set, screen, player, bubbles, clock):
    screen.fill(gm_set.bg_color)
    player.blit_me()
    for bubble in bubbles:
        bubble.blit_me()
    clock.tick(30)    
    pygame.display.flip()
