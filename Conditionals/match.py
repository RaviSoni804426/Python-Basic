num1=int(input("Enter numer1: "))
num2=int(input("Enter numer2: "))

operator =input("Enter operator: ")
match operator:
    case"+":
        print("Sum is",num1+num2)
    case"-":
        print("difference is",num1-num2)
    case"*":
        print("product is",num1*num2)

