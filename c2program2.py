f=int(input("Enter a number:"))
fib=0
first=0
second=1
print("The first", f, "numbers in the Fibonacci Series =")
print(first,"\t",second,end="\t")
for i in range(1,f-1):
    fib = first + second
    first = second
    second = fib
    print(fib,end="\t")
