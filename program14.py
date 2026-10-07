cl1=set()
cl2=set()
n1=int(input("enter limit for list1:"))
print("enter colors for list1:")
for i in range (n1):
    color=input()
    cl1.add(color)
n2=int(input("enter limit for list2:"))
print("enter colors for list2:")
for i in range (n2):
    color=input()
    cl2.add(color)
diff = cl1.difference(cl2)
print("clors=",diff)

    
