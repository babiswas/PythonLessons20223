from datetime import datetime


def get_month(dt):
   return dt.strftime("%B")

def get_weekday(dt):
   return dt.strftime("%A")

if __name__=="__main__":
  print("=====================")
  dt1=datetime.now()
  month=get_month(dt1)
  print(month)
  wd=get_weekday(dt1)
  print(wd)
  print("=====================")