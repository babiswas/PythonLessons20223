from datetime import date

def find_days(d:date)->bool:
   return (d-date(2007,10,2)).days%14==0

if __name__=="__main__":
   print("========================")
   print("Datetime:")
   date1=date(2009,10,11)
   ds=find_days(date1)
   print(ds)
   
