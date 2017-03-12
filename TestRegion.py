import string
lowercases = string.ascii_lowercase
seq = list(lowercases)
a = "-".join(seq[0:5])
print(a)

string1 = "123hello wolrd"
listA = string1.split()
for i in range(0,len(listA)):
    word = listA[i]
    listA[i] = word[0].upper() + word[1:len(word)]
s1 = " ".join(listA)
print(s1)