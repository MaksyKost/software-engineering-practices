class TennisGame1:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name: str):
        """
        Dodaje punkt do gracza
        """
        if self.player1_name == player_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def __calculate_result(self, temp_score: int) -> str:
        """
        Zwraca rachunek gracza tekstem
        """
        return {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]

    def score(self):
        """
        Zwraca cały rachunek 
        """
        result = ""
        if self.player1_points == self.player2_points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self.player2_points
            if minus_result == 1:
                result = f"Advantage {self.player1_name}"
            elif minus_result == -1:
                result = f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                result = f"Win for {self.player1_name}"
            else:
                result = f"Win for {self.player2_name}"
        else:
            result += self.__calculate_result(self.player1_points)
            result += "-"
            result += self.__calculate_result(self.player2_points)
        return result
