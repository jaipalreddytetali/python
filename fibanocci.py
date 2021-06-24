#code to print fibanocii sequence upto n terms
n = int(input("no of terms "))
n1 = 0
n2 = 1
count = 0
print("Fibonacci sequence upto ",n,":")
print("Fibonacci sequence:")
while count < n:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count=count+1
