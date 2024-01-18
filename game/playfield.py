
from game.constants import Constants

class PlayField:

    def __init__(self, width=Constants.WIDTH, height=Constants.HEIGHT, state=None):
        self.width = width
        self.height = height
        self.grid =  [""] * self.width * self.height
        if state != None:
            self.grid = state

    def get_cell(self, x, y):
        if x < 0 or (x > self.width -1): 
            raise ValueError("Invalid x argument")
        if y < 0 or (y > self.height -1):
            raise ValueError("Invalid y argument")

        index = (y * self.width) + x
        return self.grid[index]

    def set_cell(self, x, y, value):
        if not self.is_cell_playable(x, y):
            raise ValueError(f"Cannot play ${x}, ${y} as the cell is not empty")
        
        index = (y * self.width) + x
        self.grid[index] = value

    def is_win(self, token):
        r = range(self.height)
        row_won = False
        for row_index in r:
            row_won = row_won or self._is_win_row(row_index, token) 
        
        if row_won:
            return True

        col_won = False  
        r = range(self.width)
        for col_index in r:
            col_won = col_won or self._is_win_column(col_index, token)   

        if col_won:
            return True

        if self._is_win_diagonal(token):
            return True
        return False
    
    def is_stalemate(self):
        return len(list(filter(lambda x: x != Constants.PLAYER_TOKEN and x != Constants.COMPUTER_TOKEN, self.grid))) == 0

    def is_cell_playable(self, x, y):
        cell = self.get_cell(x, y) 
        return cell != Constants.PLAYER_TOKEN and cell != Constants.COMPUTER_TOKEN

    def make_deep_copy(self):
        return PlayField(width=self.width, height=self.height, state=self.grid[:])

    def print(self):
        print("====")
        print(f"{self._format_cell(0)} {self._format_cell(1)} {self._format_cell(2)}")
        print(f"{self._format_cell(3)} {self._format_cell(4)} {self._format_cell(5)}")
        print(f"{self._format_cell(6)} {self._format_cell(7)} {self._format_cell(8)}")
        print("====")

    def _is_win_row(self, row_index, token):
        for column_index in range(self.width):
            if self.get_cell(column_index, row_index) != token:
                return False
        return True
    
    def _is_win_column(self, column_index, token):
        for row_index in range(self.height):
            if self.get_cell(column_index, row_index) != token:
                return False
        return True
    
    def _is_win_diagonal(self, token):
        cross_one = True
        for diag in range(self.width):
            cross_one = cross_one and (self.get_cell(diag, diag) == token)
            
        if cross_one:
            return True
        
        cross_two = True
        indexes = reversed(range(self.width))
        for diag in indexes:
            cross_two = cross_two and (self.get_cell(diag, self.width-diag-1) == token)
                
        return cross_two

    def _format_cell(self, index):
        content = "-" if self.grid[index] == "" else self.grid[index]
        return content.rjust(2)

    def __str__(self):
        return ",".join(self.grid)