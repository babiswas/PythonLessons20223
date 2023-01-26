from collections.abc import Callable

def myfunc(a:int,b:int,add:Callable[[int,int],int])->int:
    num=add(a,b)
    return num

def add(a:int,b:int)->int:
    return a+b

def mapping_tech(mymap:dict[str,str])->None:
    for key,value in mymap.items():
        print(key,value)

if __name__=="__main__":
   print("==================")
   print("Add two numbers:")
   nm=myfunc(10,12,add)
   print(nm)
   print("==================")
   print("Displaying mapping tech:")
   mymap={"hello":"bello","mello":"tello"}
   mapping_tech(mymap)
   print("====================")