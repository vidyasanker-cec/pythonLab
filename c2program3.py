list1 = []
n = int(input("Enter the number of values in list :"))
print("Enter the elements to the list:")
for i in range(n):
    val = int(input())
    list1.append(val)
print("The sum of all items in the list is:", sum(list1))
