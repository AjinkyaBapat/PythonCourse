def sumOfPrimes(list):
    primelist = []
    sum = 0

    for i in range(0,len(list)):
        res = isPrime(list[i])
        if res is True:
            primelist.append(list[i])
            sum = sum + list[i]
    print ("Prime numbers : ", primelist)
    print ("Sum of prime numbers : ", sum)

def isPrime(n):
    factorlist = factors(n)

    if factorlist == [1,n]:
        return True
    

def factors(n):
    
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return factorlist


print("Enter list of integers separated by space")

list = [int(x) for x in input().split()]

sumOfPrimes(list)