class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def __str__(self):
    strSummary = "Rectangle(width="+ str(self.width)+", height="+str(self.height)+")"
    return strSummary
  #-------------Set methods----------------
  def set_width(self,width): self.width = width
  def set_height(self,height): self.height = height
  
  #-------------area method----------------
  def get_area(self): 
    return self.width * self.height #returns area w*h
  
  #-------------perimeter method----------------
  def get_perimeter(self): 
    return  2 * self.width + 2 * self.height
  
  #-------------diagonal method----------------
  def get_diagonal(self): 
    return (self.width ** 2 + self.height ** 2) ** .5
  
  #-------------get picture method---------------
  def get_picture(self):
    if self.width<=50 and self.height <=50:
      strPicture = ""
      for j in range(self.height):
        for i in range(self.width):
          strPicture += "*"
        strPicture += "\n"
    else: strPicture = "Too big for picture."

    return strPicture
  #------------shape inside------------
  def get_amount_inside(self,shape):
    if self.width<shape.width and self.height<shape.height: # validate free space
      return 0
    else:
      w1 = self.width
      w2 = shape.width
      h1 = self.height
      h2 = shape.height
      inTimes = 0
      #--------count times-------
      while w1>=w2 and h1>=h2:
        inTimes+=1
        if (w1-w2)>=w2: w1 = w1-w2 # verify free width space
        elif (h1-h2)>=h2: # verify free height space
          h1 = h1-h2
          w1 = self.width
        else: # not enough space / end loop
          h1 = 0
          w1 = 0
      return inTimes

class Square(Rectangle):
  def __init__(self,height):
    super().__init__(height,height)#call super class Rectangle
  def __str__(self):
    strSummary = "Square(side="+ str(self.width)+")"
    return strSummary
  def set_side(self,length):
    self.width = length
    self.height = length
  def set_width(self,width): 
    self.width = width
    self.height = width
  def set_height(self,height):
    self.width = height
    self.height = height
