def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return multiply(n,factorial(n-1))
    
def multiply(a,b):
    if b == 0:
        return 0
    else :
        return a + multiply(a,b-1)
    
n = int(input("Enter a num : "))
if n < 0:
    print("Invalid input!")
else:
    print(f"factorial of {n} is {factorial(n)}")