import pygame.font


class Scoreboard():
    
    
    def __init__(self, gm_set, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_set = gm_set
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        self.prepare_score()

    
    def prepare_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.gm_set.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20


    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)