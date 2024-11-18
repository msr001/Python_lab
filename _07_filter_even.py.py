n=[1,2,3,4,5,6,7,8,9,10]

def even_n(n):
    return n%2==0

print("Even numbers are :",list(filter(even_n,n)))