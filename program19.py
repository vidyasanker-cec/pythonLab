c=int(input("How many elements: "))
list1=[]
print("Enter the element: ")
for i in range(c):
    list1.append(int(input()))
for i in list1:
    if(i%2==0):
        list1.remove(i)
print(list1)
