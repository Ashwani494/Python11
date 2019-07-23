class Theory:
    def get_theory_marks(self):
        print("Got theory marks")


class Games:
    def get_games_marks(self):
        print("Got games marks")


class Result(Theory,Games):
    def result(self):
        print("Result calculated")

s= Result()
s.get_theory_marks()
s.get_games_marks()
s.result()