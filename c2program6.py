iString = input("Enter a string: ")
cFreq = {}
for char in iString:
    cFreq[char] = cFreq.get(char, 0) + 1
print(f"Character frequencies in '{iString}':")
for char, count in cFreq.items():
    print(f"{char} occurs {count} times.")
