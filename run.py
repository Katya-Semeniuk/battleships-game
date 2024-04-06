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




def random_point(size):
    """Helper function to return a random integer beetween 0 and size"""
    return randint(0, size -1)

def valid_coordinates(x, y, board):
    print("Valid coordinate function")

def populate_board(board):
    print("Populate board function")

def make_guess(board):
    print("make guess function")

def play_game(computer_board, player_board):
    print("Play game function")

def new_gane():
    """Starts a new game. Sets the board size and number of ships, resets the 
    scores and initializes the boards"""

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print('-' * 35)
    print("Welcome to ULTIMATE BUTTLESHIPS!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top lesft corner is row: 0, col:0")
    print('-' * 35)
    player_name = input("Enter your name...\n")
    print('-' * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)




 new_gane()

         


     


    
           







    
        


    
        



    



