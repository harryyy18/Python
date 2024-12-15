                            #MAP fUNCTION
# numbers=["3","34","334"]
# numbers=list(map(int,numbers))
# print(numbers)
# numbers[2]=numbers[2]+5
# print(numbers)     

# num=[1,2,3,4,5,6,7]
# def sq(n):
#     return n*n
# square=list(map(sq,num))
# print(square)  
#     #   OR
# num=[1,2,3,4,5,6,7]    
# square=list(map(lambda x:x*x,num))
# print(square)    

# def square(a):
#     return a*a 
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for i in range(6):
#     val=list(map(lambda x:x(i),func))
#     print(val)
                   
                     #MAP FUNCTION
# list1=[5,6,3,4,2,89,67,45,1]   
# def is_greater_5(num):
#     if num>5:
#         return num
# gr_than_5=list(filter(is_greater_5,list1))
# print(gr_than_5)                  

                    #REDUCE FUBCTION
from functools import reduce
list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
print(num)                    