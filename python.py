N=int(input("enter limit N:"))
a=0
b=1
for i in range (N):
    if a>N:
        break
    print(a,end=" ")
    a,b=b,a+b
