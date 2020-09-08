import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    #Verticals
    if self.check_line(0,1,2):
      return True
    elif self.check_line(3,4,5):
      return True
    elif self.check_line(6,7,8):
      return True
    #Horizontals
    elif self.check_line(0,3,6):
      return True
    elif self.check_line(1,4,7):
      return True
    elif self.check_line(2,5,8):
      return True
    #Diagonals
    elif self.check_line(0,4,8):
      return True
    elif self.check_line(2,4,6):
      return True
    elif self.board.count(None) == 0:
      return True
    else:
      return False

  def check_line(self, pos1, pos2, pos3):
    if (self.board[pos1] == self.board[pos2]) and (self.board[pos2] == self.board[pos3]) and self.board[pos1] != None:
      self.is_game_over = True
      if self.board[pos1] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
      else:
        self.winner = _MACHINE
      return True
    else:
      return False

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied

    # for i, cell in enumerate(self.board):
    #   if cell is None:
    #     self.board[i] = _MACHINE_SYMBOL
    #     break

    stop = False
    while stop == False:
      position = random.randint(0, 8)
      if self.board[position] is None:
        self.board[position] = _MACHINE_SYMBOL
        stop = True

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 

    matrix_board = ''
    for i in range(0, len(self.board)):
      if (i + 1) % 3 == 0:
        if self.board[i] != None:
          matrix_board += '|' + self.board[i] + ' \n'
        else:
          matrix_board += '| \n'
      else:
        if i % 3 == 0:
          if self.board[i] != None:
            matrix_board += '' + self.board[i]
          else:
            matrix_board += ' '
        else:
          if self.board[i] != None:
            matrix_board += '|' + self.board[i]
          else:
            matrix_board += '| '

    return matrix_board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if self.winner == None:
      print("No ha ganado nadie")
    else:
      print("El ganador es " + self.winner)
    pass
