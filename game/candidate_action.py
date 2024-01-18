
from game.playfield import PlayField

class CandidateAction:
    """Describe a move the computer could make and its result play state"""

    def __init__(self, play_x: int, play_y: int, token_played: str, field: PlayField):
        self.field = field
        self.play_x = play_x
        self.play_y = play_y
        self.token_played = token_played
        self.children = []
        self.computer_wins = False
        self.player_wins = False

    def add_child(self, option):
        self.children.append(option)

    def set_win_state(self, computer, player):
        self.computer_wins = computer
        self.player_wins = player