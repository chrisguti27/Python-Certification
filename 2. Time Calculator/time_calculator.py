'''
@ChristianAGutierrez
'''
def processInput(inputTime,flag = 0):
  
  if flag ==0:#start time
    aux = inputTime.split(':')
    hours = aux[0]
    minutes = aux[1]
  else:
    aux = inputTime.split(':')
    hours = aux[0]
    minutes = aux[1]
  
  return hours, minutes

def endDay(initDay,addDays):
  day = ""
  #---------Aadd Days---------------
  if initDay != ' ':
    initDay = initDay.casefold()
    initDay = initDay.capitalize()
    for i in range(addDays):
      if initDay == 'Monday':initDay = 'Tuesday'
      elif initDay == 'Tuesday':initDay = 'Wednesday'
      elif initDay == 'Wednesday':initDay = 'Thursday'
      elif initDay == 'Thursday':initDay = 'Friday'
      elif initDay == 'Friday':initDay = 'Saturday'
      elif initDay == 'Saturday':initDay = 'Sunday'
      elif initDay == 'Sunday':initDay = 'Monday'
    day = ", " + initDay
  #---------days after---------------------
  if addDays > 0: 
    if addDays<2: day = day + " (next day)"
    if addDays>=2: day = day + " (" + str(addDays) + " days later"+")"

  return day

def add_time(start, duration, initDay = " "):
  #-------- Process Input----
  am_pmStart = start.split()
  hourStart, minStart = processInput(am_pmStart[0],0)
  
  am_pmStart = am_pmStart[1]
  hourAdd, minAdd = processInput(duration,1)
  
  #----------set loops parameters----------
  minsEnd = int(minStart)
  hoursEnd = int(hourStart)
  hourAdd = int(hourAdd)
  
  #------minutes counter 0-60-------------
  for minutes in range(int(minAdd)):
    minsEnd+=1
    if minsEnd>59:
      minsEnd = 0
      hourAdd += 1
  
  minsEnd = str(minsEnd)
  #------1 digit minute------
  if len(minsEnd) < 2: 
    minsEnd = "0" + minsEnd
  
  #------hours counter 1-12-------------
  addDays = 0
  for hours in range(int(hourAdd)):  
    hoursEnd+=1
    
    if hoursEnd == 12:#change AM/PM
      if am_pmStart == 'AM': am_pmStart = 'PM'
      elif am_pmStart == 'PM': 
        am_pmStart = 'AM'
        addDays +=1
    #-------Restar hour-----------
    if hoursEnd > 12: hoursEnd = 1
      
  #-----------generate last component of the string----------
  strDay = endDay(initDay,addDays)
  
  #-----------------build output string--------------------
  new_time = str(hoursEnd) + ':' + minsEnd + ' ' + am_pmStart + strDay


  return new_time
