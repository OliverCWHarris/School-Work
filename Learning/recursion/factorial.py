def factorial(n):
    while n!=1:
        n=n*factorial(n-1);return n
    return 1
print(factorial(int(input(">"))))