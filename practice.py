n=input("Enter your credit card number:")
l=len(n)
print(f"Length of credict crd is:",l)
ls=list(n)
print(ls)

if l==16:
    i=1
    for i in ls:
        ls[i]
else:
    print("Its a fake card")