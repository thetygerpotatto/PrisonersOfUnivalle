from prisonerClasses import *

class Simulator:
    results = list(list())
    REWARDS_TABLE = [[1, 5], [0, 3]]

    def __init__(self, p1: Prisoner, p2: Prisoner, tries: int) -> None:
        self.p1 = p1
        self.p2 = p2
        self.tries = tries

    def simulate(self) -> None:
        for i in range(self.tries):
            p1_acum = 0
            p2_acum = 0
            if (i > 1):
                p1_acum = self.results[i-1][0]
                p2_acum = self.results[i-1][1]
                
            p1_play = self.p1.play()
            p2_play = self.p2.play()

            self.results.append([self.REWARDS_TABLE[p1_play][p2_play] + p1_acum
                                ,self.REWARDS_TABLE[p2_play][p1_play] + p2_acum])
            self.p1.getOponentChoice(p2_play)
            self.p2.getOponentChoice(p1_play)


