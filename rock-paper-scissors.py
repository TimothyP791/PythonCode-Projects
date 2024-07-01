class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper, scissor, android, or saiyan: " .format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock" : 0,
            "paper" : 1,
            "scissor" : 2,
            "android" : 3,
            "saiyan" : 4
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def getResultAsString(self, result):
        res = {
            0 : "draw",
            1 : "win",
            -1 : "loss"
        }
        return res[result]
    def awardPoints(self):
        print("implemnt")

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Vegeta")
        self.second_Participant = Participant("Goku")
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.second_Participant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.second_Participant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points = self.participant.points, p2name = self.second_Participant.name, p2points = self.second_Participant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.second_Participant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.second_Participant.points:
            resultString = "Winner is {name}".format(name=self.second_Participant.name)
        print(resultString)

game = Game()
game.start()