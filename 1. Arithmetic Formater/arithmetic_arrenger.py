"""
Author: Christian Gutierrez
"""
def errorCases( errorCase):
  if errorCase == 1:#Too many problems, max 5
    errorMessage = 'Error: Too many problems.'
  elif errorCase == 2:#OperatorsError
    errorMessage = 'Error: Operator must be \'+\' or \'-\'.'
  elif errorCase == 3:#OnlyNumbers
    errorMessage = 'Error: Numbers must only contain digits.'
  elif errorCase == 4:
    errorMessage = 'Error: Numbers cannot be more than four digits.'
  
  return errorMessage

def digitsValidation(number):
  for i in number:
    if ord(i) >= 48 and ord(i) <= 57:#ASCII validation
      state = True
    else:#error
      state = False
      break
  
  return state

def printOutput(listA,listB,listOperator):
  #A operator B = C
  #strA
  #strB //includes operator
  #-----------------
  #arrenged_problems = strA +'\n'+ strB + '\n'+ "---------------" + '\n'+ strResult
  strA = ""#Line1 A
  strB = ""#Line2 B
  strEquals = ""
  spaces = "    " # space between problems
  for i in range(0,len(listA)):
    
    if len(listA[i]) > len(listB[i]):
      
      whiteSpaces = len(listA[i])-len(listB[i])
      #--------------single space, operator and the longest number--------
      strA += "  " + listA[i] 
      strB += listOperator[i] #----operator in the same line of the second number
      for j in range(0,whiteSpaces+1):
        strB += " " 
      strB += listB[i]

      #---------dashes-----------
      for k in range(0,len(listA[i])+2):
        strEquals += "-"
      
    
    if len(listA[i]) < len(listB[i]):
      
      #--------------single space, operator and the longest number--------
      strA += " "#operator space
      strB += listOperator[i] #----operator in the same line of the second number
      strB += " " + listB[i]
      
      whiteSpaces = len(listB[i])-len(listA[i])
      for j in range(0,whiteSpaces+1):
        strA += " " 
      strA += listA[i]

      #---------dashes-----------
      for k in range(0,len(listB[i])+2):
        strEquals += "-"
      
    
    elif len(listA[i]) == len(listB[i]):
      #--------------single space, operator and the longest number--------
      strA += "  " + listA[i] 
      strB += listOperator[i] #----operator in the same line of the second number
      strB += " " + listB[i]
      #---------dashes-----------
      for k in range(0,len(listB[i])+2):
        strEquals += "-"
    if i <len(listA)-1:
      strA += spaces
      strB += spaces
      strEquals += spaces
      
    
  return strA +'\n'+ strB + '\n'+ strEquals

def calculatorResult (listA,listB,listOperator):
  
  strResult = ""
  spaces = "    "
  for i in range(0,len(listA)):
    #A Operator B= C
    A = int(listA[i])
    B = int(listB[i])
    aux = max(len(listA[i]),len(listB[i]))
    if listOperator[i] == '+':
      result = str(A+B)
      if len(result) > aux:
        for j in range(0, (aux+2)-len(result)):
          strResult += " " 
        strResult += result
      elif len(result) == aux:
        strResult += "  " + result
      
    elif listOperator[i] == '-': 
      strResult += " " + str(A - B)
    
    if i <len(listA)-1:
      strResult += spaces
  
  return '\n' + strResult

def arithmetic_arranger(problems, flag = False):
    #---------Split input--------#
    arranged_problems=" "
    generalVector=[]
    for i in range(0,len(problems)):
      operation = problems[i]#extract each operation
      temp = operation.split()#split a,symb,b
      generalVector += temp#accumulate each term in a list
    
    #---------------Max Problems Validation----------#
    errorCase = 0
    if len(generalVector)>15:#error
      errorCase = 1
      arranged_problems = errorCases(errorCase)
    else:  
      #----------SPLIT a,b,operators in different lists------#
      a=[]
      b=[]
      operator=[]
      for i in range(0,int(len(generalVector)/3)):

        #---------Operator Validation ------------
        if generalVector[i*3+1]== '+' or generalVector[i*3+1]=='-':
          operator.append(generalVector[i*3+1])
        else:
          errorCase = 2
          arranged_problems = errorCases(errorCase)
          break

        #---------Only Digits Validation -----------
        if digitsValidation(generalVector[i*3]) and digitsValidation(generalVector[i*3+2]):
          #----------- 4 Digits Validation---------
          if len(generalVector[i*3])<=4 and len(generalVector[i*3+2])<=4:
            a.append(generalVector[i*3])
            b.append(generalVector[i*3+2])
          else:
            errorCase = 4
            arranged_problems = errorCases(errorCase)
            break
        else:
          errorCase = 3
          arranged_problems = errorCases(errorCase=3)
          break
      if errorCase == 0:
        #---------------Print---------------
        arranged_problems = printOutput(a,b,operator)
        if flag == True:
           arranged_problems += calculatorResult(a,b,operator)
    return arranged_problems
