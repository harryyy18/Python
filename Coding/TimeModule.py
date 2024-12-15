import time
# initial=time.time()
# k=0
# while(k<45):
#     print("Hello")
#     k=k+1
# print("While loop ran in",time.time()-initial,"seconds")
# initial2=time.time()
# for i in range(0,45):
#     print("Hello")
# print("For loop ran in",time.time()-initial2,"seconds")    

localtime=time.asctime(time.localtime(time.time()))
print(localtime) 


import time 

# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i) 

# def usingFor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)


# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)    