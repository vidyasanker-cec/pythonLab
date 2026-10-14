wordList = input("Enter a list of word(comma seperated:) ").split(',')
longLen=0
for word in wordList:
    word=word.strip()
    crrntLen=len(word)
    if crrntLen > longLen:
        longLen=crrntLen
        longWord=word
print(f"longest is { longWord } with lenght { longLen }")
