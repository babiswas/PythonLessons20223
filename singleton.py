class Singleton:
   __instance=None
   
   @staticmethod
   def get_instance(params1:int,params2:int):
      if Singleton.__instance==None:
         Singleton(params1,params2)
      return Singleton.__instance

   def __init__(self,params1:int,params2:int)->None:
       self.params1=params1
       self.params2=params2
       if Singleton.__instance!=None:
          raise Exception("Already initiallised")
       else:
          Singleton.__instance=self

if __name__=="__main__":
   print("=======================")
   print("Creating Singleton:")
   instance=Singleton.get_instance(3,4)
   print(instance.__dict__)
   print("========================")