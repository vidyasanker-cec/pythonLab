num=[]
n=int(input("enter the number integers in the list:"))
print("enter the list:")
for i in range(1,n+1):
    e=int(input(""))
    if(e>100):
        num.append("over")
    else:
        num.append(e)
print("list:",num)
    
