from graphics import Line, Point

class Cell:
    def __init__(self, win= None):
      self.has_left_wall = True
      self.has_right_wall = True
      self.has_top_wall = True
      self.has_bottom_wall = True
      self._cell_size = None
      self._visited = False
      self._x1 = None
      self._x2 = None
      self._y1 = None
      self._y2 = None
      self._win = win

    def draw (self, x1, y1, x2, y2):
      if self._win is None:
        return
      self._x1 = x1
      self._x2 = x2
      self._y1 = y1
      self._y2 = y2
      if self.has_left_wall:
        l= Line(Point(x1,y1),Point(x1,y2))
        self._win.draw_line(l,"black")
      else:
        l= Line(Point(x1,y1),Point(x1,y2))
        self._win.draw_line(l,"white")

      if self.has_right_wall:
        l=Line(Point(x2,y1),Point(x2,y2))
        self._win.draw_line(l,"black")
      else:
        l=Line(Point(x2,y1),Point(x2,y2))
        self._win.draw_line(l,"white")

      if self.has_top_wall:
        l=Line(Point(x1,y1),Point(x2,y1))
        self._win.draw_line(l,"black")
      else:
        l=Line(Point(x1,y1),Point(x2,y1))
        self._win.draw_line(l,"white")

      if self.has_bottom_wall:
        l=Line(Point(x1,y2),Point(x2,y2))
        self._win.draw_line(l,"black")
      else:
        l=Line(Point(x1,y2),Point(x2,y2))
        self._win.draw_line(l,"white")
        
    def draw_move(self,to_cell, undo=False):
      
      # current cell center
      cell1_x = (self._x2 - self._x1)/2 + self._x1
      cell1_y = (self._y1 - self._y2)/2 + self._y2

      # to_cell center
      cell2_x = (to_cell._x2 - to_cell._x1)/2 + to_cell._x1
      cell2_y = (to_cell._y1 - to_cell._y2)/2 + to_cell._y2

      if undo == False:
        line_color = "red"
      else:
        line_color = "grey" 

      l_to_cell = Line(Point(cell1_x, cell1_y),Point(cell2_x, cell2_y))
      self._win.draw_line(l_to_cell, line_color)



