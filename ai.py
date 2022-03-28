import random
from enums import Moves
class AI:
  
  def __init__(self):
    self.oppMoves = ["rock"]
    self.nextMove = 0
    self.n_rock = 0
    self.n_paper = 0
    self.n_scissors = 0

  def storeMove(self, move):
    self.oppMoves.append(move)
  def checkTendencies(self):
    for i in self.oppMoves:
      if i == "rock":
        self.n_rock+=1
      if i == "paper":
        self.n_paper+=1
      if i == "scissors":
        self.n_scissors+=1
    
    if self.n_rock >= 2:
        print('Special Rock')
        self.n_rock = 0
        self.oppMoves = []
        self.nextMove = 1
        
    elif self.n_paper >= 2:
        self.n_paper = 0
        self.oppMoves = []
        self.nextMove = 2
    elif self.n_scissors >= 2:
        self.n_scissors = 0
        self.oppMoves = []
        self.nextMove = 3
    else:
      self.nextMove = Moves[random.choice(self.oppMoves)]
      
      
    if len(self.oppMoves) == 9:
        self.oppMoves = []

    return self.nextMove
        


