class Stack:
  
  def __init__(self):
    self.data = []
  
  def push(self,value):
    self.data.append(value)
    
  def pop(self):
    if len(self.data) <= 0:
      print('No elements to popup')
    else:
      self.data.pop()
   
  def peek(self):
    return self.data[0]
  
