import random 
import items, world, util

class Player():
    def __init__(self):
        self.inventory = [items.Pillow(),  items.Dagger(),items.Rock(), items.Gun(), items.SmallPotion(), items.LargePotion()] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up

        

        
        
    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
         if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
 
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)
                
                
def heal(self):
    print("\n these are the potions you currently passes.\n")
    potion_list = []
    
    for potion in self.inventory:
        if isinstance(potion, items.Potion):
            if potion.amt <= 0:
                self.inventory.remove(potion)
                continue
            else:
                potion_list.append(potion)
    i=1
    for potion in potion_list:
        print(i,". ", potion.name, sep='')
        i+=1
    while True:
        if len(potion_list) == 0: 
            print("You have no potion.")
            util.pause()
            return None
        
        
        itemChoice = util.getIntInput("""\nSelect a potion: """) - 1            
            
        if itemChoice not in range (0,len(potion_list)):
            print("\nInvalid choice")

            continue           
        break 
        
    self.healToPlayer(itemChoice, potion_list)

def healToPlayer(self, itemChoice, potionList):
    chosenPotion = potionList(itemChoice)
    util.printGameText("\nYou were healed for {} ".format(chosenPotion.health))
    util.printGameText("hp.  \n")
    self.hp = self.hp + chosenPotion.health
    chosenPotion.amt = chosenPotion.amt - 1
    if chosenPotion.amt == 0:
        self.invetory.remove(chosenPotion.health)
    
    util.pause() 
    if self.maxHp < self.hp:
        self.hp = self.maxHp       