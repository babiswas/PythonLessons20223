class User:
  def __init__(self,name:str)->None:
      self.name=name

  def update(self,article:str)->None:
      print(f"Article for user {self.name} is updated")


class User1(User):

  def __init__(self,name:str)->None:
     print("User1 has been created:")
     super().__init__(name)

class User2(User):

   def __init__(self,name:str)->None:
       print("User2 has been created:")
       super().__init__(name)


class Service:
   def __init__(self,servicename:str)->None:
       self.name=servicename
       self.subscribers=list()

   def register_subscribers(self,user:User)->None:
       self.subscribers.append(user)

   def update_subscribers(self,article:str)->None:
       for u in self.subscribers:
          u.update(article)

if __name__=="__main__":
   print("================================")
   user1=User1("user1")
   user2=User2("user2")
   service=Service("Aricle Service")
   service.register_subscribers(user1)
   service.register_subscribers(user2)
   service.update_subscribers("My article")
   print(user1.__dict__)
   print(user2.__dict__)
   print(service.__dict__)
   print("==================================")
   
   


      