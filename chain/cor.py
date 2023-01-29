from abc import ABC,abstractmethod
class Logger(ABC):

   def __init__(self,logger_object)->None:
      self.next_logger=logger_object

   @abstractmethod
   def make_entry(self,message):
       pass

   def log(self,message:str)->None:
       self.make_entry(message)
       if self.next_logger==None:
          return 
       else:
          self.next_logger.log(message)

class ConsoleLogger(Logger):
   def make_entry(self,message:str)->None:
      print("**CONSOLE**:",message)

class FileLogger(Logger):
   def make_entry(self,message:str)->None:
      print("**FILE**:",message)

class DatabaseLogger(Logger):
   def make_entry(self,message:str)->None:
      print("**DATABASE**:",message)

if __name__=="__main__":
   print("============================")
   print("**************************LOGGER UTILITY***************")
   console1=ConsoleLogger(None)
   db=DatabaseLogger(console1)
   file=FileLogger(db)
   file.log("hello")
   print("============================")
   