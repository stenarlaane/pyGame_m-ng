class GameStats():
    
    
    def __init__(self):
        self.game_active = False
        self.reset_stats()
    
    
    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.bonus = 0