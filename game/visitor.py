
from game.candidate_action import CandidateAction
from game.constants import Constants

class Visitor2:
    """Scores the different branches of the calculated tree so that the best one can be chosen"""

    def score_tree(self, parent: CandidateAction):
        self.max_score = -1
        self.max_option = None
        self.score_tree_recursive(parent, 0, 0)

    def score_tree_recursive(self, parent: CandidateAction, in_score, depth):
        if len(parent.children) == 0:
            return 0
    
        result = 0
        opt: CandidateAction
        for opt in parent.children:
            score = self.score_tree_recursive(opt, in_score, depth+1)

            # The option with the most wins take precedence
            if opt.field.is_win(Constants.COMPUTER_TOKEN):
                result = score + ((opt.field.width * opt.field.height - depth))
            else:
                result = score

            # Unless the player will win in the next turn then computer blocks
            next_move_depth = 1
            should_computer_block = opt.field.is_win(Constants.PLAYER_TOKEN) and depth == next_move_depth
            if should_computer_block:
                arbitrary_high_score = 1000
                self.max_score = arbitrary_high_score
                self.max_option = opt
            elif result > self.max_score and depth == next_move_depth:
                self.max_score = result
                self.max_option = opt

        return result
        
    def get_best_action_score(self) -> int:
        return self.max_score

    def get_best_action(self) -> CandidateAction:
        return self.max_option