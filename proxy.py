class CriticalObject:
   def __init__(self,name):
      self.name=name
      
   def __str__(self):
      return f"{self.name} is the person name"

class Proxy:
   def __init__(self):
       self.test="no"

   def access_obj(self):
       if self.test=="no":
          return None
       elif self.test=="yes":
          return CriticalObject("hello")

if __name__=="__main__":
   print("======================")
   print("Proxy design pattern:")
   p=Proxy()
   p.test="yes"
   obj=p.access_obj()
   print(obj)
   print(obj.__dict__)
   print("==========================")
     