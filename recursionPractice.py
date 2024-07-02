# 최대공약수, 피보나치 수, 팩토리얼

def GreatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a % b)


print(GreatestCommonDivisor(20, 48))
print(GreatestCommonDivisor(18, 48))
print(GreatestCommonDivisor(17, 48))
print(GreatestCommonDivisor(15, 48))


def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(10))

def Factorial(n):
    if n<=0:
        return 1
    elif n ==1:
        return 1
    else :
        return n * Factorial(n-1)
    

print(Factorial(3))