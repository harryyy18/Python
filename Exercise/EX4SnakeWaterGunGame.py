import random
lst=['s','w','g']

chance=10
no_of_chance=0
computer_pt=0
human_pt=0

print("SNAKE,WATER AND GUN GAME\n")
print("s for Snake,w for Water and g for Gun")

while no_of_chance<chance:
    _input=input("Choose from Snake,Water,Gun")
    _random=random.choice(lst)
    
    if _input==_random:
        print("Its a TIE. Both will get 0 points.")
    #If user enters s    
    elif _input=='s' and _random=='g':
        computer_pt=computer_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Computer wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")
    elif _input=='s' and _random=='w':
        human_pt=human_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Human wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")
    #If user enters w
    elif _input=='w' and _random=='s':
        computer_pt=computer_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Computer wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")
    elif _input=='w' and _random=='g':
        human_pt=human_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Human wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")
    #If user enters g
    elif _input=='g' and _random=='w':
        computer_pt=computer_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Computer wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")
    elif _input=='g' and _random=='s':
        human_pt=human_pt+1
        print(f"Your guess {_input} and computer guess {_random}.\n")
        print("Human wins 1 point.\n")
        print(f"Computer point is {computer_pt} and your point is {human_pt}\n")   
    else:
        print("You have wrong input\n")  
        
    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} chances left out of {chance}\n")   
    
print("GAME OVER")
if computer_pt==human_pt:
    print("Tie")
elif computer_pt>human_pt:
    print("Computer won")
else:
    print("Human won")    
    
print(f"Your point is {human_pt} and computers point is {computer_pt}.")             


'''
import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")

'''
