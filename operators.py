Num1=int(input("Enter a number: "))
Num2=int(input("Enter another number: "))
print("Arithmetic operators:(+,-,*,/,%,//,**)")
print("***************************************")
print("Addition(+): ",(Num1+Num2))
print("Subtraction(-): ",(Num1-Num2))
print("Multiplication(*): ",(Num1*Num2))
if(Num2!=0):
    print("Division(/): ",(Num1/Num2))
    print("Modulo Division(%): ",(Num1%Num2))
    print("Floor Division(//): ",(Num1//Num2))
else:
    print("Division(/): Cannot divide by zero")
    print("Modulo Division(%): Cannot divide by zero")
    print("Floor Division(//): Cannot divide by zero")
print("Exponentiation(**): ",(Num1**Num2))
print("---------------------------------------")
print("Logical operators:(and, or, not)")
print("***************************************")
if(Num1>Num2 and Num2<Num1):
    print("AND condition is True: Num1 is greater than Num2")
if(Num1==Num2 or Num1<Num2):
    print("OR condition is True: Either numbers are equal or Num1 is less than Num2")
if(not(Num1<Num2)):
    print("NOT condition is True: Num1 is not less than Num2")