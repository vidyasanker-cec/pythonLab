l=int(input("Enter the limit of pyramid"))
p=1
for i in range(l+1):
    p=i
    for j in range(i):
        print(p,end=" ")
        p+=i
    print("\n")
