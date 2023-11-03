from src.Enemy import Enemy

class BringerOfDeath(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, health = 40, damage = 10)
        self.exp_reward = 20

    def attack(self, player):
        pass
    
    def destroy_animation(self):
        pass