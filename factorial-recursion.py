def factorial (number):
    result = 1
    if number >1 :
        result = result * number
        return result * factorial(number-1)
    else :
        return 1


def fac(n):
    if n==1:
        return 1
    return n * fac(n-1)

print(factorial(11))
#print(fac(5))