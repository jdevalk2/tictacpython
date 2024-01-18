
from game.main import Game

def test_game_scenario1():
    game = Game()

    assert game.player_move("1,1") == None
    assert game.computer_move() == None # 0,2
    
    assert game.player_move("0,2") == None
    assert game.computer_move() == None # 0,0

    assert game.player_move("1,0") == None
    assert game.computer_move() == None # 1,2

    assert game.player_move("0,1") == None 
    assert game.computer_move() == None # 2,1

    assert game.player_move("2,2") == False # Stalemate 

def test_game_scenario2():
    game = Game()

    assert game.player_move("1,1") == None
    assert game.computer_move() == None # 2,0
    
    assert game.player_move("1,0") == None
    assert game.computer_move() == None # 1,2

    assert game.player_move("0,1") == None
    assert game.computer_move() == None # 2,1

    assert game.player_move("2,2") == None # 
    assert game.computer_move() == None # 2,1

    assert game.player_move("0,2") == False # Stalemate

def test_print():
    game = Game()
    game.playfield.set_cell(0,0,"X")
    game.playfield.set_cell(1,0,"O")
    game.playfield.set_cell(2,0,"X")
    game.playfield.print()