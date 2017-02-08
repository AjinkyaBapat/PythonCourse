#Function to reverse a positive integer

def intreverse(number) :
 Reverse = 0
 while (number>0):
  Remainder = number%10
  Reverse = (Reverse*10) + Remainder
  number = number//10
  
 return Reverse


#Function to check if brackets are matched

def matched(string) :
    stack = []
    n = 0
    flag = True

    for i in range(0,len(string)):

        if string[i] == "(":
            stack.append(string[i])
            n = n+1
        
        elif string[i] == ")":
            if n == 0:
                return False

            if stack[n-1] != "(":
                flag = False
            else:
                stack.pop(n-1)
                n = n-1

    if n != 0:
        return False
    return flag
  
  
#Function to return sum of all primes numbers in list

def sumprimes(list):
    primelist = []
    sum = 0

    for i in range(0,len(list)):
        res = isPrime(list[i])
        if res is True:
            primelist.append(list[i])
            sum = sum + list[i]
    
    return sum

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