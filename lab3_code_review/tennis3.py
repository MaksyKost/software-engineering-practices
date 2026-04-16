class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name              # p1_n --> player1_name
        self.player2_name = player2_name              # p2_n --> player2_name
        self.player1_points = 0                                     # p1 --> player1_points
        self.player2_points = 0                                     # p2 --> player2_points

    def won_point(self, player_name):
        if player_name == self.player1_name:    # "player1" --> self.player1_name
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if (self.player1_points < 4 and self.player2_points < 4) and (self.player1_points + self.player2_points < 6):
            points_names = ["Love", "Fifteen", "Thirty", "Forty"]
            score_str = points_names[self.player1_points]
            return score_str + "-All" if (self.player1_points == self.player2_points) else score_str + "-" + points_names[self.player2_points]
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            winner_name = self.player1_name if self.player1_points > self.player2_points else self.player2_name
            return (
                "Advantage " + winner_name
                if ((self.player1_points - self.player2_points) * (self.player1_points - self.player2_points) == 1)
                else "Win for " + winner_name
            )

player1='Ona'
player2='On'
game = TennisGame3(player1, player2)
game.won_point(player2)
game.won_point(player2)
game.won_point(player1)
print(game.score())