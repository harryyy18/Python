"""FALSE CALCULATOR
   45*3=555
   56+9=77
   56/6=4
"""   
print("Enter 1st number")
num1=int(input())
print("Enter 2st number")
num2=int(input())
print("Out of the following which operation do you want to perform:","+,-,*,/,%")
op=input()
if(num1==45 and num2==3 and op=='*'):
    print(f"{num1}*{num2}=555")
elif(num1==56 and num2==9 and op=='+'):
   print((f"{num1}{num2}=77"))  
elif(num1==56 and num2==6 and op=='/'):
   print((f"{num1}/{num2}=4"))
elif(op=='+'):
   plus=num1+num2
   print(plus)
elif(op=='-'):
   sub=num1-num2
   print(sub)
elif(op=='*'):
   mul=num1*num2
   print(mul)
elif(op=='%'):
   mod=num1%num2
   print(mod)
elif(op=='/'):
   div=num1/num2 
   print(div)
else:
   print("Error!!....")                      
