
# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value ):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description,self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
    
    
    def sound(self):  # weapon can have own sound"
        pass
 
class Potion(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.health)
 
class SmallPotion(Potion):
    def __init__(self):
        super().__init__(name = "small Potion",
                         description="A small Potion",
                         value=5,
                         amt=1,
                         health =25)
        
class LargePotion(Potion):
    def __init__(self):
        super().__init__(name = "large Potion",
                         description="A small Potion",
                         value=5,
                         amt=1,
                         health =30)
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)

 
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
class Pillow(Weapon):
    def __init__(self):
        super().__init__(name="Pillow",
                         description="A pillow super soft.",
                         value=1,
                         damage=1)
        
class Gun(Weapon):
    def __init__(self):
        super().__init__(name="Gun",
                         description="A Big gun with full bullet. Somewhat more dangerous than all.",
                         value=10,
                         damage=10)
        
