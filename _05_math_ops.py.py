def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

while True:
    print("Arithmetic Operations")
    print("1 to add.\n2 to sub.\n3 to mul.\n4 to div.\n5 to exit.")
    n = int(input("Enter number:\n"))

    if n == 5:
        print("Exiting the program.")
        break

    n1 = int(input("Enter num1: "))
    n2 = int(input("Enter num2: "))

    if n == 1:
        print("Sum of entered numbers is:", add(n1, n2))
    elif n == 2:
        print("Difference of entered numbers is:", sub(n1, n2))
    elif n == 3:
        print("Product of entered numbers is:", mul(n1, n2))
    elif n == 4:
        print("Division of entered numbers is:", div(n1, n2))
    else:
        print("Wrong number. Enter between 1 to 4 only.")
