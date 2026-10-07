dict1={}
dict2={}
print("\nEnter the values dict1")
while True:
    key=input("Enter the key(or q for quit):")
    if key=='q':
        break
    dict1[key]=int(input("Enter the value:"))

print("\n\nEnter the values for dict2")
while True:
    key=input("Enter the key(or q for quit):")
    if key=='q':
        break
    dict2[key]=int(input("Enter the value:"))

print(dict1|dict2)
