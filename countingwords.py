introString = input("Enter Your Introduction: ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if (i==' '):
        wordCount=wordCount+1
print("Number Of Words: ")
print(wordCount)
print("Number Of Characters: ")
print(characterCount)