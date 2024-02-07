cp=int(input("Enter cost price:"))
sp=int(input("Enter selling price:"))

if cp>sp:
    loss=cp-sp
    print("Loss is",loss)
elif sp>cp:
    profit=sp-cp
    print("Profit is",profit)
else:
    print("no profit no loss")