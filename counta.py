names=[]
counts=0
n=int(input("enter the number of namea:"))
print("enter list of names:")
for i in range(1,n+1):
      e=input()
      names.append(e)
for name in names:
      counts+=name.lower().count('a')
print(counts)
