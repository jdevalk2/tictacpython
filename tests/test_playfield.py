
from game.playfield import PlayField

def test_cross():
    field = PlayField(state = ["X", "", "", "", "X", "", "", "", "X"])
    result = field._is_win_diagonal("X")
    assert result == True

    field =  PlayField(state = ["", "", "X", "", "X", "", "X", "", ""])
    result = field._is_win_diagonal("X")
    assert result == True

def test_horizontal():
    field1 = PlayField(state = ["X", "X", "X", "", "", "", "", "", ""])
    result = field1._is_win_row(0, "X")
    assert result == True

    field2 = PlayField(state = ["", "", "" ,"X", "X", "X", "", "", ""])
    result = field2._is_win_row(1, "X")
    assert result == True

    field3 = PlayField(state = ["", "", "" ,"", "", "", "X", "X", "X"])
    result = field3._is_win_row(2, "X")
    assert result == True

def test_horizontal2():
    field1 = PlayField(width=2, height=2, state = ["X", "X", "", ""])
    result = field1._is_win_row(0, "X")
    assert result == True

    field2 = PlayField(width=2, height=2, state = ["", "", "X", "X"])
    result = field2._is_win_row(1, "X")
    assert result == True

def test_vertical():
    field1 = PlayField(state = ["X", "", "", "X", "", "", "X", "", ""])
    result = field1._is_win_column(0, "X")
    assert result == True

    field2 = PlayField(state = ["", "X", "" ,"", "X", "", "", "X", ""])
    result = field2._is_win_column(1, "X")
    assert result == True

    field3 = PlayField(state = ["", "", "X" ,"", "", "X", "", "", "X"])
    result = field3._is_win_column(2, "X")
    assert result == True
    
    