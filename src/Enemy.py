
class Enemy():
    def __init__(self, x, y, health, damage):
        self.position = (x,y)
        self.health = health
        self.damage = damage

    def attack(self):
        pass

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        pass