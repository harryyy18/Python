def funargs(*args):
    for item in args:
        print(item)
list=["Harry","Dhariya","Aaditya"]
funargs(*list)      

def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)
list=["Harry","Dhariya","Aaditya"] 
normal="The following are my roommates"
funargs(normal,*list) 

def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("My roomates Favourite food are as following:\n")
    for key,value in kwargs.items():
        print(f"{key} loves {value}")    
list=["Harry","Dhariya","Aaditya"]
dictionary={"Harry":"Pizza","Dhariya":"Maggiee","Aaditya":"AlooPuri"} 
normal="The following are my roommates"
funargs(normal,*list,**dictionary)        