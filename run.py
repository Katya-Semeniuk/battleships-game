scores = {"computer": 0, "player": 0}

class Board:
     """Main Board Class. Sets board size, the number of ships, 
     the player`s name and the board type (player board or computer)
     Has methods for adding ships and quesses and printing the board"""

     def __init__(self, size, num_ships, name, type):
          self.size = size
          self.board = [['.' for x in range(size)] for y in range(size)]
          self.num_ships = num_ships
          self.name = name
          self.type = type
          self.guesses = []
          self.ships = []
     
     def print(self):
          for row in self.board:
           print(''.join(row))

     def guess(self, x, y):
          self.guess.append((x, y))
          self.board[x][y] = 'X'

          if (x, y) in self.ships:
               self.board[x][y] = '*'
               return "Hit"
          else:
           return "Miss"
          

     def add_ships(self, x, y, type="computer"):
         if len(self.ships) >= self.num_ships:
             print("Error: you cannot add any more ships!")
         else:
             self.ships.append((x, y))
             if self.type == 'player':
                 self.board [x][y] = '@'
         


     


    
           







    
        


    
        



    


