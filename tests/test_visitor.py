
from game.visitor import Visitor2
from game.candidate_action import CandidateAction
from game.playfield import PlayField
from game.constants import Constants

def test_visito_scoring():
    v = Visitor2()
    op = CandidateAction(0, 0, Constants.PLAYER_TOKEN, PlayField(3, 3, ["X", "", "", "", "", "", "", "", ""]))
    oc1 = CandidateAction(1, 0, Constants.COMPUTER_TOKEN, PlayField(3, 3, ["X", "O", "", "", "", "", "", "", ""]))
    op.add_child(oc1)
    oc2 = CandidateAction(1, 0, Constants.PLAYER_TOKEN, PlayField(3, 3, ["X", "O", "X", "", "", "", "", "", ""]))
    oc1.add_child(oc2)
    oc3 = CandidateAction(1, 0, Constants.COMPUTER_TOKEN, PlayField(3, 3, ["X", "O", "X", "", "O", "", "", "", ""]))
    oc2.add_child(oc3)
    oc4 = CandidateAction(1, 0, Constants.PLAYER_TOKEN, PlayField(3, 3, ["X", "O", "X", "X", "O", "", "", "", ""]))
    oc3.add_child(oc4)
    oc4 = CandidateAction(1, 0, Constants.COMPUTER_TOKEN, PlayField(3, 3, ["X", "O", "X", "X", "O", "", "", "O", ""]))
    oc3.add_child(oc4)
    v.score_tree(op)
    
    assert v.get_best_action_score() == 6
    best_action = v.get_best_action()
    assert best_action.play_x == 1 
    assert best_action.play_y == 0
    
  