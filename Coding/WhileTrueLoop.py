while True:
    name = input("Enter customers name: ")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount: "))
        quantity = float(input("Enter the quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items?(yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-" * 40)
    print("Name: ", name)
    print("amount to be paid: ", total)
    print("-" * 40)
    print("******Happy Shopping******")

    repeat1 = input("Do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break

