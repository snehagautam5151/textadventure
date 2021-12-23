class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0
class Zombies(Enemy):
    def __init__(self):
        super().__init__(name="Zombies", hp=10, damage=2)
 
class Monster(Enemy):
    def __init__(self):
        super().__init__(name="Monster", hp=10, damage=15)

class Crocodile(Enemy):
    def __init__(self):
        super().__init__(name="Crocodile", hp=20, damage=10)

class GroomyHunter(Enemy):
    def __init__(self):
        super().__init__(name="GroomyHunter", hp=25, damage=15)
        
class Monkey(Enemy):
    def __init__(self):
        super().__init__(name="Monkey", hp=10, damage=5)
        
class Octopus(Enemy):
    def __init__(self):
        super().__init__(name="Octopus", hp=15, damage=5)
        
class Shark(Enemy):
    def __init__(self):
        super().__init__(name="Shark", hp=10, damage=5)
        
class MonsterFish(Enemy):
    def __init__(self):
        super().__init__(name="MonsterFish", hp=10, damage=5)
        
class Pirahna(Enemy):
    def __init__(self):
        super().__init__(name="Pirahna", hp=10, damage=5)
        
class ZombiesFish(Enemy):
    def __init__(self):
        super().__init__(name="ZombiesFish", hp=10, damage=5)
        
class Snake(Enemy):
    def __init__(self):
        super().__init__(name="Snake", hp=15, damage=25)
        
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="GiantSpider", hp=15, damage=25)
        
class Scorpio(Enemy):
    def __init__(self):
        super().__init__(name="Scorpio", hp=15, damage=20)
        
class DeartCreature(Enemy):
    def __init__(self):
        super().__init__(name="DeartCreature", hp=15, damage=20)
        
class Python(Enemy):
    def __init__(self):
        super().__init__(name="Python", hp=15, damage=20)
        
class NinjaAttack(Enemy):
    def __init__(self):
        super().__init__(name="NinjaAttack", hp=15, damage=20)
        
class BadBee(Enemy):
    def __init__(self):
        super().__init__(name="BadBee", hp=15, damage=20)
        
class BadMan(Enemy):
    def __init__(self):
        super().__init__(name="BadMan", hp=15, damage=20)
        
