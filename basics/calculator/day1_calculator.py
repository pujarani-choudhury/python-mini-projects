#A simple CLI-based calculator for beginners

#Step-1 :- Define functions for operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "❌ cann't divide by zero"
    return a/b

#Step-2 :- Loop for repeated calculation
while True:
    print("\nSimple CLI Calculator")
    print("Operations :- + - * /")
    print("Type 'q' to quit")

    op = input("Enter operation (+, -, *, / or q):")
    if op == 'q':
        print("Goodbye")
        break   #exit the loop

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter Second number:"))


#Step-3 :- Perform Calculation
    if op == '+':
        print("Result:", add(num1, num2))
    elif op == '-':
        print("Result:", substact(num1, num2))
    elif op == '*':
        print("Result:", multiply(num1, num2))
    elif op == '/':
        if num2 == 0:
            print("❌ cann't divide by zero")
        else:
            print("Result:", divide(num1, num2))
    else:
        print("❌ Invalid Operation. Please try again.")



