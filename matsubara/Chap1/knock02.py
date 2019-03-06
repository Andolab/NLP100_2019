str1 = "パトカー"
str2 = "タクシー"
newstr = ""
for i, j in zip(str1, str2):
    newstr += i + j
print(newstr)
