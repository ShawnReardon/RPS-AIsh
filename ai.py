import random
from enums import Moves
class AI:
  
  def __init__(self, name):
    self.name = name
    self.oppMoves = ["rock"]
    self.nextMove = 0
    self.n_rock = 0
    self.n_paper = 0
    self.n_scissors = 0
    self.wonLastTurn = False
    self.isDraw = False

  def resetCnts(self):
    self.n_rock = 0
    self.n_paper = 0
    self.n_scissors = 0
  def storeMove(self, move):
    self.oppMoves.append(move)
  def won(self):
    self.wonLastTurn = True
    self.isDraw = False
  def lost(self):
    self.wonLastTurn = False
    self.isDraw = False
  def draw(self):
    self.isDraw = True
  def checkTendencies(self):
    i = self.oppMoves[len(self.oppMoves) - 1]
    if i == "rock":
        self.n_rock+=1
    if i == "paper":
        self.n_paper+=1
    if i == "scissors":
        self.n_scissors+=1
    if random.randint(0, 9) > 7:
      print('\n***CHANCE***')
      self.nextMove = random.randint(1,3)
      return self.nextMove
    if self.wonLastTurn: #may remove
      return self.nextMove
    elif self.isDraw:
      print('\nEducated Guess i: ', i, self.name)
      self.isDraw = False
      if i == 'rock':
        
        self.nextMove = 2
        return self.nextMove
      elif i == 'paper':
        
        self.nextMove = 3
        return self.nextMove
      elif i == 'scissors':
        
        self.nextMove = 1
        return self.nextMove
      
      
    if self.n_rock >= 2:
        #print('Special Rock')
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
      
      
    if len(self.oppMoves) >= 4:
        self.oppMoves = []

    
      

    return self.nextMove
        


