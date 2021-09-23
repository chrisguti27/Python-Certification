"""
author: Christian A. Gutierrez
"""
import copy # shallow or deep copy of a list 
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**args):#**args: dictionary
    self.contents = []
    colors = [] # list of color in the hat
    quantity = [] # number of each ball color in the hat
    for balls in args:
      colors.append(balls)
      quantity.append(args[balls])
    #----------- fill content list -----------
    for i in range(len(colors)):
      for j in range(quantity[i]):
        self.contents.append(colors[i])
  
  #---------draw method------------
  def draw(self,numDraw):
    if numDraw > len(self.contents): return self.contents
    else:
      drawBalls = random.sample(self.contents,k = numDraw)
      #use ramdom.sample() no random.choices()!!!!
      for ballOut in drawBalls:
        self.contents.remove(ballOut)  
      return drawBalls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #hat is Hat object
  #expected_balls is dictionary
  probability = 0
  N = num_experiments
  M = 0
  colors = []
  quantity = []
  expectedBalls = []
  # -------create list of expected balls with self.content format
  for balls in expected_balls:
      colors.append(balls)
      quantity.append(expected_balls[balls])
    #----------- fill content list -----------
  for i in range(len(colors)):
    for j in range(quantity[i]):
      expectedBalls.append(colors[i])
  
  expectedList = copy.copy(expectedBalls)
  #print(expectedList)
  initial_hat = copy.deepcopy(hat.contents)
  #----------experiments-----------
  for i in range(N):
    getBalls = hat.draw(num_balls_drawn)
    j = 0
    #------count time when drawing out expected balls-----
    while j < len(getBalls) and len(expectedList)>0:
      for wish in expectedList:
        if getBalls[j] == wish: expectedList.remove(getBalls[j]) 
      if expectedList == []: M +=1
      j += 1
    #-------set new experiment-----
    expectedList = copy.copy(expectedBalls)
    hat.contents = copy.copy(initial_hat) # newExperiment
  
  probability = M/N

  print(probability)
  return probability
