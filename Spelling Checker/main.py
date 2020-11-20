from textblob import TextBlob

file1 = open("spell.txt","r+")

a = file1.read()

print(str(a))
b = TextBlob(a)

print("corrected text : ", str(b.correct()))

d = open("spell.txt", "w")
d.write(str(b.correct()))
d.close()