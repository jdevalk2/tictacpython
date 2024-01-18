
from game.playfield import PlayField
from game.tree import TreeBuilder
from game.candidate_action import CandidateAction
from game.visitor import Visitor2
from game.constants import Constants

class Game:
    """Entry point for Tic Tac Toe game"""

    def __init__(self):
        self.playfield = PlayField(width=Constants.WIDTH, height=Constants.HEIGHT)

    def player_move(self, player_input: str) -> bool:
        x, y = self.parse_input(player_input)
        
        self.playfield.set_cell(x, y, Constants.PLAYER_TOKEN)
        if self.playfield.is_win(Constants.PLAYER_TOKEN):
            return True
        
        if self.playfield.is_stalemate():
            return False

        return None

    def computer_move(self):
        arbitrary_input = "-1,-1"
        x, y = self.parse_input(arbitrary_input)

        tree_builder = TreeBuilder(Constants.WIDTH, Constants.HEIGHT)
        board_copy = self.playfield.make_deep_copy()
        option = CandidateAction(x, y, Constants.PLAYER_TOKEN, board_copy)
        tree_builder.build_tree(option, Constants.COMPUTER_TOKEN)

        visitor = Visitor2()
        visitor.score_tree(option)

        best_option = visitor.get_best_action()
        self.playfield.set_cell(best_option.play_x, best_option.play_y, Constants.COMPUTER_TOKEN) 

        if self.playfield.is_win(Constants.COMPUTER_TOKEN):
            return True
        
        if self.playfield.is_stalemate():
            return False
        
        return None
    
    def parse_input(self, player_input: str):
        input = player_input.split(",") # 1,2 format
        x = int(input[0])
        y = int(input[1])
        return x, y
    
    def loop(self):
        """Alternate between computer and player turns until a result is reached or QUIT"""

        text = ""
        game.playfield.print()
        
        while text != "QUIT":    
            print("Your next move X,Y? [0-2],[0-2] or QUIT")
            text = input()
            
            pm = self.player_move(text)
            game.playfield.print()
            if pm is None:
                pass
            elif not pm:
                print("Stalemate!")
                break
            elif pm:
                print("You won!")
                break

            print("Computer is thinking ...")
            cm = self.computer_move()
            game.playfield.print()
            if cm is None:
                pass
            elif not cm:
                print("Stalemate!")
                break
            elif cm:
                print("Computer won!")
                break

if __name__ == "__main__":
    game = Game()
    game.loop()