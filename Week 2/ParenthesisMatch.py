string = input("Enter a string: ")

def isMatching(string):
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

result = isMatching(string)

if result is True:
    print ("True")
else:
    print ("False")

