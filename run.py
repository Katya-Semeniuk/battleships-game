from random import randint

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
          self.guesses.append((x, y))
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
    """ Inside converts all string values into integers
    Reises ValueError if strings cannot be converted into int"""
    try:
        row = int(x)
        column = int(y)

        if row < 0 or row >= board.size or column < 0 or column >= board.size:
            print(
                f"Values must be between 0 and {board.size - 1}"
            )
            return False

    except ValueError as e:
        print('Coordinates must be integers\n')
        return False

    return True
        
    


def populate_board(board):
    """ Populating board for computer and for player.
    Using a random number from the random_point function, ships are added to the board"""
    while True:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ships(x, y)
            break      
       
     
           
def make_guess(board):
    """ sets random coordinates for the computer's guess
      and retrieves data from the imput for the user"""
    while True:
        if board.type == 'computer':
            x = random_point(board.size)
            y = random_point(board.size)
            return x, y
        else:
            row = input("Guess a row: \n")
            column = input("Guess a column: \n")

            if valid_coordinates(row, column, board):
                return int(row), int(column)
            else:
                print('Input IS NOT correct')



def play_game(computer_board, player_board, scores):
    """ Shows the board of the player and the computer, 
launches a function to determine the coordinates of the opponent's ship
and displays the result of the game with the update of points"""

    while True:
        print(f"{player_board.name}'s Board")
        player_board.print()
        
        print(f"{computer_board.name}'s Board")
        computer_board.print()

        # player's part
        player_guess = make_guess(player_board)
        print("Player guessed", player_guess)
        if player_guess:
            player_result = computer_board.guess(*player_guess)
            if player_result == "Miss":
                print("Player missed this time")
            else:
                scores["player"] += 1
                print("Player won this time")
            
        
        # computer's part
        computer_guess = make_guess(computer_board)
        print("Computer guessed", computer_guess)
        if computer_guess:
            computer_result = player_board.guess(*computer_guess)
            if computer_result == "Miss":
                print("Computer missed this time")
            else:
                scores["computer"] += 1
                print("Computer won this time")
        

        print('-' * 35)
        print("After this round, the score are:")
        print(f"{player_board.name} {scores['player']} . {computer_board.name} {scores['computer']}")
        print('-' * 35)
        
        input("Enter any key to continue ")
        print('-' * 35)



def new_game():
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

    """Creates two class instances"""
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    print(player_board.ships)
    print(computer_board.ships)
    play_game(computer_board, player_board, scores)
    
    

new_game()

    
           







    
        


    
        



    



