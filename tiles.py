import items, enemies, actions, world
import winsound

 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


    
class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """  

                
        .##       ########.########..######.
        .##.......##..........##....##....##
        .##.......##..........##....##......
        .##.......######......##.....######.
        .##.......##..........##..........##
        .##.......##..........##....##....##
        .########.########....##.....######.
        ..######..########....###....########..########...
        .##....##....##......##.##...##.....##....##......
        .##..........##.....##...##..##.....##....##......
        ..######.....##....##.....##.########.....##......
        .......##....##....#########.##...##......##......
        .##....##....##....##.....##.##....##.....##......
        ..######.....##....##.....##.##.....##....##......

    
    
      
        You find yourself in a big city a brilliant scientist, is a survivor of a man-made 
        plague that transforms humans into bloodthirsty mutants. He wanders alone through New York City,
        calling out for other possible survivors, and works on finding a cure for the plague using his 
        own immune blood. Neville knows he is badly outnumbered and the odds are against him, and all
        the while,the infected wait for him to make a mistake that will deliver Neville into their hands.
        You could say that the dark-seekers have been observing him the whole time and set up a trap for him by placing Fred there as a lure/bait. 
        That would likely be the most plausible explanation"""
        
    winsound.PlaySound( "worrior_Gods.wav", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyHall(MapTile):
    def intro_text(self):
        return """
        This is a path winding therough a dimly lit building. 
        the way heads 3 direction ,one perticularly
        large area with some low light at the edge of the path 
        "WHICH PATH YOU WOULD LIKE TO CHOOSE EAST OR WEST"
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class CrocodileRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crocodile())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Crocodile jumps down in front of you!e
             """
        else:
            return """
             The corpse of a dead Crocodile is on the ground.
             """

    
class MonkeyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Monkey())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound( "monkey.wav", winsound.SND_FILENAME)
            return """
             A  monkeys juamp down in front of you! and want to snatch you mobile and your bag and yout stuff 
             """
             
        else:
            return """
        
             The corpse of a dead monekys and blood are every where on the ground.
  
             """
             
class ZombiesRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombies())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A zombies jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead zombies rots on the ground.
            """
class MonsterRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Monster())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A monster jumps down from its  in front of you!"""
        else:
            return """
            The corpse of a dead monsterrots on the ground.
            """
            
class DaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
                        ,,,,,,,,,,,,,,,,,s
                        ,,,,,,,,,,,,,,,,sss
                        ,,,,,,,,,,,,,,,,sss
                        ,,,,,,,,,,,,,,,sssss
                        ,,,,,,,,,,,,,,,sssss
                        ,,,,,,,,,,,,,,,sssss
                        ,,,,,,,,,,,,,,sssssss
                        ,,,,,,,,,,,,,,sssssss
                        ,,,,,,,,,,,,,,sssssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,ss,,,,sssssssss,,,,sss
                        ,,,,,sss,,,,,ssssssss,,,,,sss
                        ,,,ssss,,,,,sssssssss,,,,,ssss
                        ,,,sssssssssssssssssssssssss
                        ,,,,,,,,,,,,,,ssssssss
                        ,,,,,,,,,,,,,,,ssssss
                        ,,,,,,,,,,,,,,,ssssss
                        ,,,,,,,,,,,,,,,ssssss
                        ,,,,,,,,,,,,,,ssssssss
                        ,,,,,,,,,,,,,,,,sssss
                        ,,,,,,,,,,,,,sssssssss
                        ,,,,,,,,,,,,,,,ssssss

    
    
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        as you can see there are many weapon are there like sord and knife, 
        plate and bowl, and taddybear , mobile and which one you would like to pick'
         
        """  

class LeaveBuilding(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
        &^$&^*&*&(^&^&^&&&877)
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
        
       
       
 
class BigOcean(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in big ocean with empty gun and but in next styage will get bullets... 
                         ______________________________
                _____ __/ /   ^^ __ ___________________|
               / \ \@([          ___]_________)
              |____/\----[______]
            //    |    / ((  )
            /_____|:------:
            \_____
               
               
               Your notice something rusty in the corner.
        It's a GUN! You pick it up.
        as you can see there are many weapon are there like box and knife, 
        plate and bowl, and dagger ,  pick one '
        """
        
    winsound.PlaySound( "Heys", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass       

        
        
class Cave(MapTile):
    def intro_text(self):
        return """
        This deep cave where you have to go through fro next level
        "WHICH PATH YOU WOULD LIKE TO CHOOSE EAST OR WEST"
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass        
        

class GunRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gun())
 
    def intro_text(self):
        return """      
        
        
                    ^^ __ ___________________,
                \ \@([            ]_________)
                _/\----[______]
            //        / ((    )
            /_____|:------:
            \_____/
        
    
        Your notice something rusty in the corner.
        It's a GUN! You pick it up.
        as you can see there are many weapon are there like box and knife, 
        plate and bowl, and dagger ,  pick one '
         
        """ 
        
class Cave(MapTile):
    def intro_text(self):
        return """
        This deep cave where you have to go through fro next level
        "WHICH PATH YOU WOULD LIKE TO CHOOSE EAST OR WEST"
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass          

    
class OctopusRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Octopus())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A octopus is front of you,
                                    
                                    ░░░░░░░░░░░║
                        ░░▄█▀▄░░░░░║░░░░░░▄▀▄▄
                        ░░░░░░▀▄░░░║░░░░▄▀
                        ░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄
                        ▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
                        ░░░░░░██░░▀▐▌▀░░██
                        ░▄█▀▀▀████████████▀▀▀█
                        █░░░░░░██████████░░░░░▀▄
                        █▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
                        ░▀█░░░█░░░░░░░░░░█░░░█▀

            
            
            
            
            !
            """
        else:
            return """
            The corpse of a dead Octopus on the ground."""  

class SharkRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Shark())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A shark is front of you, !
            """
        else:
            return """
            dead Shark on the ground."""
            
            
class MonsterFishRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MonsterFish())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A group of monster fish is coming so be prepare             
            <*͜)͜͡˒͜ ͡˒ ⋊  f <*͜)͜͡˒͜ ͡˒ ⋊    <*͜)͜͡˒͜ ͡˒ ⋊   <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊            
            <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊   <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊
            <*͜)͜͡˒͜ ͡˒ ⋊ <*͜)͜͡˒͜ ͡˒ ⋊    <*͜)͜͡˒͜ ͡˒ ⋊   <*͜)͜͡˒͜ ͡˒ ⋊  f  <*͜)͜͡˒͜ ͡˒ ⋊  <*͜)͜͡˒͜ ͡˒ ⋊    <*͜)͜͡˒͜ ͡˒ ⋊
            """
        else:
            return """
                  deah fish all arround    <*͜)͜͡˒͜ ͡˒ ⋊a """
 

  
class PirahnaRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Pirahna())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A group of monster fish is coming so be prepare  !
            """
        else:
            return """
                  deah fish all arround """                
                  
                  
class ZombiesFishRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ZombiesFish())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A zombies fishes  front of you!
            """
        else:
            return """
            The corpse of a dead zombies Fish rots on the ground.
            """
class EmptyOcean(MapTile):
    def intro_text(self):
        return """
        you can see empty ocean and find direction 
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
             


class LeaveOceans(MapTile):
    def intro_text(self):
        return """
        You see a bright iceland  in the distance...
        ... it grows as you get closer! It's sunlight!
        you are out of ocean and you hgot victory 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
        
        
class EnterInDesert(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You find yourself in big Desert there are many camel nearby so you can ride on them and one mobile with low battery.
        
        
        
                        __¶¶¶¶_______¶¶¶___¶¶¶¶¶
                _¶¶¶¶¶¶_____¶¶¶___¶¶¶¶¶¶¶
                ¶¶¶_¶¶¶¶___¶¶¶__¶¶¶¶____¶
                ¶____¶¶¶¶_¶¶¶¶_¶¶¶¶
                _______¶¶_¶¶¶¶_¶¶¶_¶¶¶¶¶¶¶
                ____¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_¶¶¶¶¶
                ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶
                __¶¶¶__¶¶¶¶¶¶¶¶¶¶__________¶
                ¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                ¶¶__¶¶¶¶__¶¶¶¶_¶¶_¶¶¶¶
                ¶__¶¶¶¶___¶¶¶__¶¶___¶¶¶¶
                ___¶¶¶____¶¶¶___¶¶____¶¶¶
                ___¶¶__¶__¶¶¶___¶¶¶_____¶¶_____§§
                ___¶___¶¶__¶¶¶___¶¶¶_____¶____§§§§
                ____¶¶¶¶¶¶__¶¶____¶¶¶________§§§§§§
                ___¶¶¶¶¶¶¶¶__¶_____¶¶¶______§§§§§§§§
                __¶¶¶¶¶¶¶¶¶¶________¶¶¶____§§§§§§§§§§¶¶
                ___¶¶__¶¶¶¶¶_________¶¶¶__§§§§§§§§§§¶¶¶¶
                ___¶___¶¶¶¶___________¶¶¶§§§§§§§§§§¶¶¶¶¶¶
                ___¶__¶¶¶¶_____________¶¶¶_______¶¶¶¶¶¶¶¶¶
                ___¶__¶¶¶¶______________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶
                ___¶_¶¶¶¶________________¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶
                ___¶_¶¶¶¶¶_______¶¶¶¶¶____¶¶¶
                ___¶_¶¶¶¶¶______¶¶¶¶¶¶¶____¶¶¶
                ___¶_¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶____¶¶¶
                ___¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶
                ____¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶
                _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶
                _______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶
                ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶
                ________¶¶¶¶¶¶______¶¶¶¶¶¶¶____¶¶¶
                _________¶¶¶¶________¶¶¶¶¶¶____¶¶¶
                _________¶¶¶_________¶¶¶¶¶_____¶¶¶
                _________¶¶¶__________¶¶¶______¶¶¶
                _________¶¶¶__________¶¶¶_____¶¶¶
                _________¶¶¶___________¶¶_____¶¶¶
                _________¶¶¶___________¶¶____¶¶¶
                ________¶¶¶__________¶¶¶__¶¶¶¶¶ 
        
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass  
    
    
class CamelRide(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
       There are a great many ways for visitors to discover 
       the magic of Morocco's incredible city of Marrakesh,
       and you may find your adventure much more exciting 
       when you choose to explore by way of a traditional 
       camel ride. and after reached there your second level will start.
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass  
     

    
class BottelOfWater(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
        
       after getting sord here, there are many stuff . which is found in old crash plan, there are many things
       somthing old cheez and onw wine of bottle but empty and skelton might be of pilot and 2 or 3 bottle of water luckly few are left.
        he kept all the stuff and bpottle with him whch were fround in the crash plane.
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
             winsound.PlaySound( "Creature.wav", winsound.SND_FILENAME)
             return """
            A  giant spider is front of you. he wants to eat you !
            """
        else:
            return """
            Dead spider on the ground.
            """

class SnakeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Snake())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A snake is front of you,he wants to bite you!
            """
        else:
            return """
            you kill the snake and his body on the ground.
            """


class ScorpioRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Scorpio())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A zombies fishes  front of you!
            """
        else:
            return """
            The corpse of a dead zombies Fish rots on the ground.
            """

class fire(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
        in next stage, its dark night in desert so he suddenly find some stcik of fire, with the help of this he can 
        see the way
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 


           

class BadBeeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BadBee())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A BadBee  front of you!
            """
        else:
            return """
            you have killed the Bee
            """          
class NinjaAttackRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.NinjaAttack())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A BadBee  front of you!
            """
        else:
            return """
            you have killed the Bee"""
           

    
    

    
class cave(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
      The wav of cave want to go east or west
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
class EnterInCave(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
      enter in cave . choose direction 
      xa
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
 
class ExitFromCave(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
      Exit From Cave . choose direction 
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
        
class Strom(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
      the big strom is on the way you want to choose east 
      and west or nort direction to save your lufe from sand strom 
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
class ExistFRomCave(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
     now we have exit from cave 
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
    
    
class WaterFall(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
     there is very samll waterfall where u can drink water choose east or west wh
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
class BadManRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BadMan())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A BadMan is front of you,he wants to kill you!
            """
        else:
            return """
            you kill the Badman and his body on the ground.
            """
            
class EmptyWay(MapTile):
        # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
     there is long desert path and choose  direction 
      
        
        """
        
    winsound.PlaySound( "hey", winsound.SND_FILENAME)
 
    def modify_player(self, player):
        #Room has no action on player
        pass 
    
class ExitDesert(MapTile):
    def intro_text(self):
        return """
        You see a city 
        ... it grows as you get closer! It's sunlight!
        you are out of Desert and you got victory 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
        
        

    
class LargePotionRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.largePotion())
 
    def intro_text(self):
        return """
    
    this is small potion"""

class CavePath(MapTile):
    def intro_text(self):
        return """
        Enter in Cave 
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass


class SmallPotionRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.SmallPotion())
 
    def intro_text(self):
        return """
    
    this is small potion"""
    
    
class DesertCretureRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DeartCreature())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A DesertCreature  front of you!
            """
        else:
            return """
            you have killed the craeture"""


class Fire(MapTile):
    def intro_text(self):
        return """
        fire of wood, relax and go  
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass                
    
class Fire(MapTile):
    def intro_text(self):
        return """
        fire of wood, relax and go  
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    
