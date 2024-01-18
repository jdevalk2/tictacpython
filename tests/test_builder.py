
from game.tree import TreeBuilder
from game.candidate_action import CandidateAction
from game.playfield import PlayField
from game.visitor import Visitor2
from game.constants import Constants

def test_builder_level_one():
    tb = TreeBuilder(width=2, height=2)
    opt = CandidateAction(0, 0, Constants.PLAYER_TOKEN, PlayField(2, 2, [Constants.PLAYER_TOKEN, "", "", ""]))
    tb.build_tree_recursive(opt, Constants.COMPUTER_TOKEN, 0, 1)

    assert len(opt.children) == 3
    assert str(opt.children[0].field) == "X,,O,"
    assert opt.children[0].computer_wins == False
    assert opt.children[0].player_wins == False

    assert str(opt.children[1].field) == "X,O,,"
    assert opt.children[1].computer_wins == False
    assert opt.children[1].player_wins == False

    assert str(opt.children[2].field) == "X,,,O"
    assert opt.children[2].computer_wins == False
    assert opt.children[2].player_wins == False

def test_builder_level_two():
    tb = TreeBuilder(width=2, height=2)
    opt = CandidateAction(0, 0, Constants.PLAYER_TOKEN, PlayField(2, 2, [Constants.PLAYER_TOKEN, "", "", ""]))
    tb.build_tree_recursive(opt, Constants.COMPUTER_TOKEN, 0, 2)

    assert len(opt.children) == 3
    assert str(opt.children[0].field) == "X,,O,"

    assert str(opt.children[0].children[0].field) == "X,X,O,"
    assert str(opt.children[0].children[1].field) == "X,,O,X"

    assert str(opt.children[1].field) == "X,O,,"

    assert str(opt.children[1].children[0].field) == "X,O,X,"
    assert str(opt.children[1].children[1].field) == "X,O,,X"

    assert str(opt.children[2].field) == "X,,,O"

    assert str(opt.children[2].children[0].field) == "X,,X,O"
    assert str(opt.children[2].children[1].field) == "X,X,,O"

def test_builder_integration_no_computer_win():
    tb = TreeBuilder(width=2, height=2)
    opt = CandidateAction(0, 0, Constants.PLAYER_TOKEN, PlayField(2, 2, [Constants.PLAYER_TOKEN, "", "", ""]))
    tb.build_tree_recursive(opt, Constants.COMPUTER_TOKEN, 0, 2)

    v = Visitor2()
    v.score_tree(opt)
    best_option = v.get_best_action()
    assert v.get_best_action_score() == 1000
    assert best_option.play_x == 1
    assert best_option.play_y == 0

def test_builder_integration_with_computer_win():
    tb = TreeBuilder(width=2, height=2)
    opt = CandidateAction(0, 0, Constants.COMPUTER_TOKEN, PlayField(2, 2, [Constants.COMPUTER_TOKEN, "", "", ""]))
    tb.build_tree_recursive(opt, Constants.PLAYER_TOKEN, 0, 2)

    v = Visitor2()
    v.score_tree(opt)
    best_option = v.get_best_action()
    assert v.get_best_action_score() == 3
    assert best_option.play_x == 1
    assert best_option.play_y == 0

