n=21
no_of_guess=1
print("You can guess only 9 times..")
while(no_of_guess<=9):
    num=int(input("Enter the number:\n"))
    if num>21:
        print("Decrement your guessing number.\n")
    elif num<21:
        print("Incremnt your guessing number\n")
    else:
        print("You Won..")
        print("You took",no_of_guess,"guesses to guess the number.")
        break   
    print("Number of Guesses left",9-no_of_guess)
    no_of_guess=no_of_guess+1
if no_of_guess>9:
    print("Game Over")         
