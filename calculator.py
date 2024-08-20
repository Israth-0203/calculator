print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")
option=int(input("enter your choice to perform calculation:"))

if(option in[1,2,3,4]):
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

    if(option==1):
        result = num1 + num2
    elif(option==2):
        result = num1 - num2
    elif(option==3):
        result = num1 * num2
    elif(option==4):
        result = num1 // num2

else:
    print("invalid operation!")

print("the result of the performed opration is {}".format(result))
