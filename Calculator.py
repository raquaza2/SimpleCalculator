def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x/y

operator = input("Enter an operator(+ - * /):")

x = float(input("Enter 1st number:"))
y = float(input("Enter 2nd number:"))

if operator == "+":
    print(add(x,y))
elif operator =="-":
    print(subtract(x,y))
elif operator == "*":
    print(multiply(x,y))
elif operator == "/":
    print(divide(x,y))




