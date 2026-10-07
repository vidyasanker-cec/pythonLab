result = []
start = int(input("Enter the starting range (four-digit number): "))
end = int(input("Enter the ending range (four-digit number): "))

if start<999 or end>10000 or end<start:
    print("Invalid range. Please enter a valid four-digit range.")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
            if root*root==num:
                result.append(num)
    print("Four-digit even perfect square numbers in the given range:")
    print(result)
