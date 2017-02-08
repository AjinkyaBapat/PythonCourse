#Python program to reverse a positive integer

def intreverse(number) :
 Reverse=0
 while (number>0):
  Remainder = number%10
  Reverse = (Reverse*10) + Remainder
  number = number//10
 print(Reverse)
 return

number = int(input("Enter an integer: "))

if(number>0):
 intreverse(number)

else:
 print("Number must be positive integer");	