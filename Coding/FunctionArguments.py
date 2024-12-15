# #There are 4 types of function arguments:
# default
# keyword
# variable length
# reguired

#DEFAULT ARGUMENTS   
def avg(a=5,b=10):
    print((a+b)/2)
avg(4,6) 
avg(6,8)
avg(6)
avg(b=5)  
print("\n")

#KEYWORD ARGUMENTS  order doesn't matters
def avg(a=4,b=6):
    print((a+b)/2)
avg(b=9,a=3) 
avg() 
print("\n")  


#REQUIRED ARGUMENTS   order is mandatory for required parameters
def avg(a,b=6):
    print((a+b)/2)
avg(2) 
avg(2,b=10)     
avg(a=6,b=6)

#VARIABLE LENGTH ARGUMENTS  it is like args and kwargs
