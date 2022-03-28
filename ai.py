import random
from enums import Moves
class AI:
  
  def __init__(self):
    self.oppMoves = ["rock"]
    self.nextMove = 0
    self.n_rock = 0
    self.n_paper = 0
    self.n_scissors = 0

  def resetCnts(self):
    self.n_rock = 0
    self.n_paper = 0
    self.n_scissors = 0
  def storeMove(self, move):
    self.oppMoves.append(move)
  def checkTendencies(self):
    i = self.oppMoves[len(self.oppMoves) - 1]
    if i == "rock":
        self.n_rock+=1
    if i == "paper":
        self.n_paper+=1
    if i == "scissors":
        self.n_scissors+=1
    
    if self.n_rock >= 2:
        print('Special Rock')
        self.resetCnts()
        self.oppMoves = []
        self.nextMove = 1
        
    elif self.n_paper >= 2:
        self.resetCnts()
        self.oppMoves = []
        self.nextMove = 2
    elif self.n_scissors >= 2:
        self.resetCnts()
        self.oppMoves = []
        self.nextMove = 3
    else:
      self.nextMove = Moves[random.choice(self.oppMoves)]
      
      
    if len(self.oppMoves) == 9:
        self.oppMoves = []

    if random.randint(0, 9) == 0:
      print('***CHANCE***')
      self.nextMove = random.randint(1,3)
      

    return self.nextMove
        


