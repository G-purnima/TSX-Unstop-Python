length=float(input("Enter length: "))
width=float(input("Enter width: "))
if(length<=0 or width<=0):
    print("Length and width must be positive numbers only.")
else:
    area=length*width
    perimeter=2*(length+width)
    print("Area of a Rectangle:",area)
    print("Perimeter of a Rectangle:",perimeter)