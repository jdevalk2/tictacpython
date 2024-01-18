
from game.candidate_action import CandidateAction
from game.constants import Constants

class TreeBuilder:

    computer_token = "O"
    player_token = "X"

    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height

    def build_tree(self, board: CandidateAction, plays_next_token):
        self.build_tree_recursive(board, plays_next_token, 0, None)

    def build_tree_recursive(self, option: CandidateAction, turn_token: str, depth: int, max_depth: int):
        
        for x in range(0, self.width):
            for y in range(0, self.height):
                if option.field.is_cell_playable(x, y):
                    field_copy = option.field.make_deep_copy()
                    field_copy.set_cell(x, y, turn_token)

                    new_option = CandidateAction(x, y, turn_token, field_copy)
                    option.add_child(new_option)

                    computer_win = new_option.field.is_win(Constants.COMPUTER_TOKEN) 
                    player_win = new_option.field.is_win(Constants.PLAYER_TOKEN)
                    option.set_win_state(computer_win, player_win)

                    if not (computer_win or player_win):
                        if turn_token == Constants.PLAYER_TOKEN:
                            next_token = Constants.COMPUTER_TOKEN
                        else:
                            next_token = Constants.PLAYER_TOKEN
                        
                        if (max_depth is None) or (depth+1 < max_depth):
                            self.build_tree_recursive(new_option, next_token, depth + 1, max_depth)

    


