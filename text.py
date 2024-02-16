class CricketScoresheet:
    def __init__(self, team1, team2, total_overs):
        self.team1 = team1
        self.team2 = team2
        self.total_overs = total_overs
        self.current_over = 0
        self.current_ball = 0
        self.team1_runs = 0
        self.team2_runs = 0
        self.team1_wickets = 0
        self.team2_wickets = 0
        self.team1_overs_bowled = 0
        self.team2_overs_bowled = 0
        self.team1_scorecard = []
        self.team2_scorecard = []

    def record_runs(self, runs):
        if self.current_over >= self.total_overs:
            print("Match over!")
            return

        if self.team1_wickets == 10 or self.team2_wickets == 10:
            print("All out!")
            return

        if self.current_ball == 6:
            self.current_over += 1
            self.current_ball = 0

        if self.current_over % 2 == 0:
            self.team1_runs += runs
            self.team1_scorecard.append(runs)
        else:
            self.team2_runs += runs
            self.team2_scorecard.append(runs)

        self.current_ball += 1

    def record_wicket(self):
        if self.current_over >= self.total_overs:
            print("Match over!")
            return

        if self.team1_wickets == 10 or self.team2_wickets == 10:
            print("All out!")
            return

        if self.current_over % 2 == 0:
            self.team1_wickets += 1
            self.team1_scorecard.append("W")
        else:
            self.team2_wickets += 1
            self.team2_scorecard.append("W")

        self.current_ball += 1

    def display_scorecard(self):
        print("Team 1 Scorecard:", self.team1_scorecard)
        print("Team 2 Scorecard:", self.team2_scorecard)
        print("Team 1 Runs:", self.team1_runs)
        print("Team 2 Runs:", self.team2_runs)
        print("Team 1 Wickets:", self.team1_wickets)
        print("Team 2 Wickets:", self.team2_wickets)
        print("Team 1 Overs Bowled:", self.team1_overs_bowled)
        print("Team 2 Overs Bowled:", self.team2_overs_bowled)


# Example usage
scoresheet = CricketScoresheet("Team A", "Team B", 10)
scoresheet.record_runs(1)
scoresheet.record_runs(2)
scoresheet.record_runs(4)
scoresheet.record_wicket()
scoresheet.record_runs(6)
scoresheet.record_runs(0)
scoresheet.display_scorecard()
