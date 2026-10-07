sentence=input("enter the sentence")
words=sentence.split()
counts={}
for i in words:
    if i in counts:
        counts[i]+=1
    else :
        counts[i]=1
print(counts)
