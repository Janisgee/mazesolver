from cell import Cell
import time
import random

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win= None, seed = None):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed:
      random.seed(seed)

    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    self._reset_cells_visited()

  def _create_cells(self):
    # fill a self._cells list with lists of cells.
    # Call _draw_cell() method on each Cell.
    for row in range (0, self._num_rows):
      self._cells.append([])
      for col in range (0, self._num_cols):
        cell = Cell(self._win)
        self._cells[row].append(cell)
    
    for row in range (0 , self._num_rows):
      for col in range (0, self._num_cols):
        self._draw_cell(row, col)
        
    

  def _draw_cell(self, i, j):
    # calculate the x/y position of Cell base on i, j and cell size, draw the cell 
    # and call the maze's _animate()
    if self._win is None:
      return 
    cell_x1 = self._x1 + j * self._cell_size_x
    cell_y1 = self._y1 + i * self._cell_size_y
    cell_x2 = cell_x1 + self._cell_size_x
    cell_y2 = cell_y1 + self._cell_size_y

    cell = self._cells[i][j]

    cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
    self._animate()

  def _animate(self):
    # call window's redraw() method
    # sleep for a short amount of time ->Keep up with each render frame.
    # (slept for 0.05 seconds)
    if self._win is None:
      return 
    self._win.redraw()
    time.sleep(0.01)

  def _break_entrance_and_exit(self):
    # Remove an outer wall of entrance and exit cells
    # Call _draw_cell() after each removal
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall= False
    self._draw_cell(self._num_rows-1, self._num_cols-1)

  def _break_walls_r(self, i, j):
    # Mark current cell as visited
    self._cells[i][j]._visited = True

    # Loop infinite
    while True:
      possible_directions = []
      
      #check adjacent cells to current cell.
      #Left cell
      if i > 0 and not self._cells[i-1][j]._visited:
        possible_directions.append((i-1,j))
      #Right cell
      if i < self._num_rows-1 and not self._cells[i+1][j]._visited:
        possible_directions.append((i+1,j))
      #down cell
      if j < self._num_cols-1 and not self._cells[i][j+1]._visited:
        possible_directions.append((i,j+1))
      #up cell
      if j > 0 and not self._cells[i][j-1]._visited:
        possible_directions.append((i, j-1))
      
      # if no possible direction, break out.
      if len(possible_directions) == 0:
        self._draw_cell(i,j)
        return
      
      # Ramdomly choose the next direction to go
      pick_index = random.randrange(len(possible_directions))
      pick_cell = possible_directions[pick_index]

      # adjacent cell position to current cell
      # Right
      if pick_cell[1] == j + 1:
        self._cells[i][j].has_right_wall = False
        self._cells[i][j + 1].has_left_wall = False
      # Left
      if pick_cell[1] == j - 1:
        self._cells[i][j].has_left_wall = False
        self._cells[i][j - 1].has_right_wall = False
      # Down
      if pick_cell[0] == i + 1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[i + 1][j].has_top_wall = False
      # Up
      if pick_cell[0] == i - 1:
        self._cells[i][j].has_top_wall = False
        self._cells[i - 1][j].has_bottom_wall = False

      # self._draw_cell(i,j)
      # self._draw_cell(pick_cell[0],pick_cell[1])

      #Recursively call to move to chosen cell
      self._break_walls_r(pick_cell[0],pick_cell[1])

  def _reset_cells_visited(self):
    
    for row in self._cells:
      for cell in row:
        cell._visited = False

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    # Return True if current cell is end cell
    # Return False if current cell is loser cell
    self._animate()
    self._cells[i][j]._visited = True
    if i == self._num_rows-1 and j == self._num_cols-1:
      return True
    
    cell = self._cells[i][j]
    # Top
    if i-1 >= 0 and not cell.has_top_wall and not self._cells[i-1][j]._visited:
      cell.draw_move(self._cells[i-1][j])
      if self._solve_r(i-1,j):
        return True
      else:
        cell.draw_move(self._cells[i-1][j], undo = True)

    # Bottom
    if i+1 <= self._num_rows -1 and not cell.has_bottom_wall and not self._cells[i+1][j]._visited: 
      cell.draw_move(self._cells[i+1][j])
      if self._solve_r(i+1,j):
        return True
      else:
        cell.draw_move(self._cells[i+1][j], undo = True)

    # Right
    if j+1 <= self._num_cols -1 and not cell.has_right_wall and not self._cells[i][j+1]._visited:
      cell.draw_move(self._cells[i][j+1])
      if self._solve_r(i,j+1):
        return True
      else:
        cell.draw_move(self._cells[i][j+1], undo = True)
    
    # Lift
    if j-1 >= 0 and not cell.has_left_wall and not self._cells[i][j-1]._visited:
      cell.draw_move(self._cells[i][j-1])
      if self._solve_r(i,j-1):
        return True
      else:
        cell.draw_move(self._cells[i][j-1], undo = True)
    
    return False

        

      
         
      


      


