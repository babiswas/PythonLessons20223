class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

  def get_dict(self):
     return self.__dict__

if __name__=="__main__":
   print("============================")
   obj=A(3,4)
   print(obj.get_dict())
   print(obj)
   print("==============================")