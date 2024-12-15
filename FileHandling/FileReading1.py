                                #READING FILE"
# f=open("harry.txt","r+")
# content=f.read()
# print(content)
# f.close

# f=open("harry.txt","r+")
# content=f.read(3)
# print(content)
# content=f.read(2)
# print(content)
# f.close

# f=open("harry.txt","r+")
# for line in f:
#     print(line,end=" ")
# f.close()


# f=open("harry.txt","r+")
# print(f.readline())
# # print(f.readline())
# f.close()

# f=open("harry.txt","r+")
# print(f.readlines())
# f.close()

                                    #WRITING FILE"
# f=open("harry.txt","w")     #It will replace the older content
# f.write("Heyy how r u\n") 
# f.close()
# f=open("harry.txt","a")  #It will append and not replace
# f.write("thank you\n")
# f.close()
                 
# f=open("harry.txt","a")
# a=f.write("hello")
# print(a)
# f.close() 

# f=open("harry.txt","r+") #Here it will not replace while writing
# print(f.read())
# f.write("\nHHHHHHHHH")  

# f=open("harry.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(16)
# print(f.readline())  
# f.close()                     

                    #USING "WITH"
# with open("harry.txt") as f:
#     a=f.read(6)
#     print(a) 
    
with open("harry.txt") as f:
    a=f.readlines()
    print(a)    
f=open("harry.txt","rt")
a=f.readline()
print(a)                       