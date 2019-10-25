str1 = 'パトカー'
str2 = 'タクシー'
result = ''
for (a, b) in zip(str1, str2):
    result += a + b
print(result)
