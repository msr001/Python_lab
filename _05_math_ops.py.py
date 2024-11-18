def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    print("Arithmetic Operations 😊
    print("1 to add.\n2 to sub.\n3 to mul.\n4 to div.\n")
    n=int(input("Enter number :\n"))
    n1=int(input("Enter num1 :"))
    n2=int(input("Enter num2 :"))

if n==1:
    print("Add of entered numbers is :",add(n1,n2))

elif n==2:
    print("Minus of entered numbers is :",sub(n1,n2))

elif n==3:
    print("Multiply of entered numbers is :",mul(n1,n2))

elif n==4:
    print("Divide of entered numbers is :",div(n1,n2))

else:
    print("Wrong number. ENter between 1 to 4 only")