#Calc
#CODE BY LUCKY

num1 = int(input("Enter 1st Number : "))
operator = input("Enter Operator : ")
num2 = int(input("Enter 2nd Number : "))

if(operator == "+"):
    print("Addition = ",num1+num2)
elif(operator == "-"):
    print("Subtraction = ",num1-num2)
elif(operator == "*"):
    print("Multiplication = ",num1*num2)
elif(operator == "/"):
    if num2 != 0:
        print("Division = ", num1/num2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid Input")
#End of programe
