def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a + b)


def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a - b)


def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a * b)


def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a / b)


on = True
while on:
    operation = input("please type +, -, *,/ or q ")
    if operation == "+":
        addition()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    elif operation == "q":
        on = False
    else:
        print("Wrong operation, please try again")
