"""
Author: Christian A. Gutierrez
"""

class Category:

  def __init__(self,categories):
    self.ledger = []
    self.categories = categories # food,clothing,entertainment
    self.balance = 0 #current balance
  
  def __str__(self):
    
    title =  self.categories
    title = title.center(30,'*')#center title
    strSummary = title + '\n'
    detail = "{description}{amount}"
    for movement in self.ledger:
      movementD = movement["description"]
      movementA = "{:.2f}"# 2 point decimal resoluton
      movementA = movementA.format(movement["amount"])
      if len(movementD) > 23 : movementD = movementD[:23]#max 23 characteres
      if len(movementA) > 7 : movementA = movementA[:8]#max 7 characters
      #------------build each output line--------------
      temp = detail.format(description = movementD.ljust(23," "), amount = movementA.rjust(7," "))
      
      strSummary = strSummary + temp + '\n'
    #--------------add total line------------
    total = "Total: {:.2f}"
    total = total.format(self.balance)
    strSummary += total
    return strSummary
  
  def deposit(self,amount,description = ""):
    
    self.ledger.insert(0,{"amount": float(amount), "description": description})
    self.get_balance() #update balance
  
  def withdraw(self,amount,description = ""):
    
    if self.balance >= float(amount): # validate funds
      self.ledger.append({"amount": -amount, "description": description})
      self.get_balance() #update balance
      return True
    else: return False
  
  def get_balance(self):
    
    auxBal = 0
    for movement in self.ledger:
      amount = movement["amount"]
      auxBal += float(amount)
    self.balance = auxBal
    return self.balance

  def transfer(self,amount,budget):
    state = self.withdraw(amount,"Transfer to " + budget.categories)
    if state == True:
      budget.deposit(amount,"Transfer from " + self.categories)
      return True
    else: return False
  
  def check_funds(self,amount):
    if amount > self.balance: return False
    else: return True 
    

def create_spend_chart(categories): #categories is a list with objects type Category

  strPlot = "Percentage spent by category\n"
  scaleList = ["100|"," 90|"," 80|"," 70|"," 60|"," 50|"," 40|"," 30|"," 20|"," 10|","  0|"]
  
  #----------calculate percentajes----------
  total = 0
  percentages = []
  labels = []
  for category in categories:
    auxBal = 0
    for movement in category.ledger: #get ledger
      amount = movement["amount"]
      if float(amount)<0:auxBal += float(amount)
    percentages.append(auxBal)
    total += auxBal
    labels.append(category.categories)#extract categories names
  
  bars = []
  for i in range(len(percentages)):
    percentages[i] = percentages[i] / total
    aux = int(int(percentages[i]*100)/10)
    bar = []
    #-----------create bars----------
    for j in range(aux + 1):
      bar.append("o")
    for j in range(10-aux):
      bar.insert(0," ")
    
    bars.append(bar)
    
  #--------------build bar plot------------
  for i in range(len(scaleList)):
    strBars = ""
    for j in range(len(bars)):
      aux = bars[j]
      aux = aux[i]
      strBars += " " + aux + " "
    lineFormat = scaleList[i] + strBars
    strPlot = strPlot + lineFormat +" \n"
  
  #----------------build label------------------
  strLabel = "    "
  maxLabel = 0
  for i in range(len(percentages)):
    strLabel = strLabel + "---"
    aux = labels[i]
    aux = list(aux)
    if len(aux)> maxLabel: maxLabel =len(aux) 
    labels[i] = aux
  strPlot = strPlot + strLabel + "-"
  #----------------plot labels---------------
  for i in range(maxLabel):
    strLabel="   "
    for j in range(len(labels)):
      aux = labels[j]
      try : aux = aux[i]
      except: aux = " "
      strLabel += " " + aux + " "
    lineFormat = "\n " + strLabel + " "
    strPlot = strPlot + lineFormat
  
  return strPlot
