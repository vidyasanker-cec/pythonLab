list1=[]
list2=[]
n1=int(input("enter the no. of integers in list 1:"))
print("enter the integers of list 1:")
for i in range(1,n1+1):
    e=int(input())
    list1.append(e)
n2=int(input("enter the no. of integers in list 2:"))
print("enter the integers of list 2:")
for i in range(1,n2+1):
    e=int(input())
    list2.append(e)
print("list1:",list1)
print("list2:",list2)
if len(list1) == len(list2):
    print("both list same no. of elements")
else:
    print("not equal")
if sum(list1)==sum(list2):
    print("sum of both list are same")
else:
    print("not same")


