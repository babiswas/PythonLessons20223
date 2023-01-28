import re
class SampleText:
   def __init__(self,str1:str)->None:
       self.str1=str1

   def format_text(self)->str:
       self.str1.strip()
       return self.str1

class ProcessNames(SampleText):
    stop_words=["The","Indian","Beginning","Conclusion","Telugu","Tamil","Works","Arka","Media"]

    def __init__(self,str1:str)->None:
        super().__init__(str1)


    def process(self):
        self.process_names()
     
    def process_names(self)->None:
        self.str1=self.format_text()
        pattern="[A-Z][a-z]+"
        words=re.findall(pattern,self.str1)
        name_filter=list(filter(lambda test: test not in ProcessNames.stop_words,words))
        print("Displaying all names:")
        for wd in name_filter:
            print(wd)


class ProcessActors(SampleText):
    upper_case=[chr(65+i) for i in range(0,26)]

    def __init__(self,str1:str)->None:
        super().__init__(str1)


    def process(self):
        self.process_actors()
     
    def process_actors(self)->None:
        self.str1=self.format_text()
        pattern="Rana[\s]+[A-Za-z\,\s]+\."
        sentences=re.findall(pattern,self.str1)
        for s in sentences:
            names=s.split(',')
            print(names)

class TextProcessor:

    def __init__(self)->None:
        self.processors=list()

    def register(self,obj:SampleText)->None:
        self.processors.append(obj)

    def process_all_text(self)->None:
        for obj in self.processors:
            obj.process()

class Solution:

    @classmethod
    def try_text(cls):
        str1=input("Enter the text:")
        objects=[ProcessNames(str1),ProcessActors(str1)]
        proc=TextProcessor()
        for obj in objects:
            proc.register(obj)
        proc.process_all_text()
        
        
        
        
if __name__=="__main__":
   print("===================================")
   Solution.try_text()
   print("===================================")
   


       

