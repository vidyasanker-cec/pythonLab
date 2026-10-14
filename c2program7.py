iString=input("Enter a string")
if iString.endswith("ing"):
    modString= iString+"ly"
else:
    modString= iString+"ing"
print("modified strig is:",modString)
