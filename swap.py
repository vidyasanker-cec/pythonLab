string1=input("enter a string1")
n=len(string1)
first=string1[0]
last=string1[n-1]
mod_str=last + string1[1:n-1] + first
print(mod_str)

              
