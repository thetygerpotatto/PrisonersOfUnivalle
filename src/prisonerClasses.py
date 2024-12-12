import random

class Prisoner:
    def play(self):
        if (random.random() < 0.5):
            return 1
        else: 
            return 0
    def getOponentChoice(self, choice: int):
        pass

class tit_for_that(Prisoner):
    betray = False
    def play(self):
        if self.betray:
            self.betray = False
            return 0
        else: 
            return 1
    def getOponentChoice(self, choice: int):
        if (choice): self.betray = False
        else: self.betray = True

class steve(Prisoner):
    op_coop = 0
    def play(self):
        if random.random()*100 < 20: return 0
        if (self.op_coop >= 5): return 0
        else: return 1
