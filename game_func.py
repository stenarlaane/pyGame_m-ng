import pygame
import sys
from bubble import Bubble


pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)


def check_events(gm_set, screen, player, bubbles, stats, play_button):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, bubbles)


def check_play_button(stats, play_button, mouse_x, mouse_y, bubbles):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


def create_bubble(gm_set, screen, bubbles):
    new_bubble = Bubble(screen, gm_set)
    bubbles.add(new_bubble)


def update_bubbles(player, bubbles, stats, sb, gm_set):
    hitted_bubble = pygame.sprite.spritecollideany(player, bubbles)
    if hitted_bubble != None:
        stats.score += hitted_bubble.bubble_radius
        sb.prepare_score()
        if (int(stats.score / gm_set.bonus_score)) > stats.bonus:
            stats.level += 1
            sb.prepare_level()
            stats.bonus += 1
        hitted_bubble.kill()


def update_screen(gm_set, screen, player, bubbles, clock, stats, play_button, sb):
    screen.fill(gm_set.bg_color)
    player.blit_me()
    if len(bubbles) > 0:
        for bubble in bubbles:
            bubble.blit_me()
    sb.draw_score()
    clock.tick(30)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
