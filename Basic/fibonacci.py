def fibonacii(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)
n=int(input("Enter n: "))
for i in range(1,n+1):
  print(fibonacii(i))
