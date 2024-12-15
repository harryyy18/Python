questions=[["Who invented Java Language","Harry","Jeemy","James Gosling","Guido Van Rossum",3],
["Who invented Python Language","Harry","Jeemy","James Gosling","Guido Van Rossum",4],
["Which is national bird of india","Harry","Peacock","James Gosling","Guido Van Rossum",2],
["Which is national animal of india","Tiger","Peacock","James Gosling","Guido Van Rossum",1],
["Which is national flower of india","Harry","Peacock","Lotus","Guido Van Rossum",3],
["How many states in india","34","32","29","28",3],
["Who invented C Language","Harry","Danish Ritchie","James Gosling","Guido Van Rossum",2],
["Who is winner of wrestlemania 2024","Cody","james","Roman","Dean",1],
["Who is called the Father of Science","Harry","Newton","Einstein","Thomas alva Adision",3],
["Pet name of Virat Kohli","Viru","Koku","Chintu","Chiku",4]]

levels=[1000,2000,3000,4000,10000,20000,40000,80000,160000,320000]
money=0

for i in range(0,len(questions)):
    print(f"{i+1} question for Rupees {levels[i]} is:")
    question=questions[i]
    print(question[0])
    print(f"1.{question[1]}                2.{question[2]}")
    print(f"3.{question[3]}                4.{question[4]}")
    rep=int(input("Choose the correct option or 0 to quit:"))
    
    if(rep==0):
        money=levels[i-1]
        break
    if(rep==question[-1]):
        print(f"Well Played. Aap jith te hai {levels[i]} rupee\nBadhte Hai Agle prashna ki Aur...\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000    
    else:
        print("Galat Jawab\n")
        if(i>=0 and i<4):
            money=0
        elif(i>=4 and i<9):
            money=10000
        else:
            money=320000        
        break
    
print(f"Badhai Hoi. App {money} ki Dhanrashi Ghar le ke jayenge.") 
print("Aapka KBC ka safar yahi samapt hua... ") 
print("Dhnayawad")          
    
    