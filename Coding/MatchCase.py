x=int(input("Enter any number"))
match x:
    case 0:
        print("X is ",x)
    case 1:
        print("X is ",x+1)
    case 4:
        print("X is ",x+2) 
    case _:
        print("Default Case1")           