def fibo(n):
    # base case
    if n <= 0:
       return  print("Incorrect input")
    
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibo(n-1) +fibo(n-2)

print(fibo(1))