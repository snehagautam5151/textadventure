
from player import Player

_world = {}
starting_position = (0, 0)
 
def load_tiles():
    
    
    """Parses a file that describes the world space into the _world object"""
    
    print("""welcome the Text adventure world
          
          ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  

████████╗███████╗██╗░░██╗████████╗  ░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝  ██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░  ███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░
░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░  ██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░  ██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝

░░░░░██╗░█████╗░██╗░░░██╗██████╗░███╗░░██╗███████╗██╗░░░██╗
░░░░░██║██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝
░░░░░██║██║░░██║██║░░░██║██████╔╝██╔██╗██║█████╗░░░╚████╔╝░
██╗░░██║██║░░██║██║░░░██║██╔══██╗██║╚████║██╔══╝░░░░╚██╔╝░░
╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚███║███████╗░░░██║░░░
░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
          
          
          
          
          ..""")

    level_input = int(input('ENTER YOUR LEVEL :'))
    print(level_input)
    if level_input == 1: 
        print("you have enterance level 1")
    elif level_input == 2:
        print("you have enternece level 2")
        Player.level = level_input
    else:
        print("enter level 3")
    if level_input == 2:
        
        with open('mapone.txt','r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
                if tile_name == 'BigOcean':            
                    global starting_position
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            
    
    elif level_input == 1:
        
        with open('map2.txt','r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
                if tile_name == 'StartingRoom':                      
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
      
    else :
        
        with open('map3.txt','r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace("\r\n", "\n") # Windows users may need to replace '\r\n'
                if tile_name == 'EnterInDesert':  
                                      
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)          
                

    
def tile_exists(x, y):
    return _world.get((x, y))