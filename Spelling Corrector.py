from textblob import TextBlob
file = open('Incorrect Spelling.txt')
a = file.read()
print("original text : "+str(a))
b = TextBlob(a)
print("Corrected Text :"+str(b.correct()))
file.close()

d = open('Incorrect Spelling.txt','w')
d.write(str(b.correct()))
d.close()
