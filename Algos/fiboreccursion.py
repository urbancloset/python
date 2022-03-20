def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

number = 10
if number <=0:
    print("Enter Number Greater Than Zero")
else:
    print("Fibonacci Series:")
    for x in range(number):
        print(fibo(x))
