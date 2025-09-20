num1 = float(input("enter the firstnumber: "))
num2 = float(input("enter the second number: "))
operation= input("enter an operation (+.-,*,/): ")


if operation == "+":
        result =num1 + num2
        print(f"{num1} + {num2} = {result}")

elif operation =="-":
        result = num1 - num2
        print(f"{num1} - {num2} ={result}")

elif operation =="/":
    if num2 !=0:
        result = num1 /num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print(" Invallid operation. Please enter +, -, *, or /.")