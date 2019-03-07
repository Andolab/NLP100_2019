s = "Hi He Lied Because Boron Could Not Oxidize \
    Fluorine. New Nations Might Also Sign Peace \
    Security Clause. Arthur King Can."
words = s.split()
number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
token = {}
for i in range(0, len(words)):  # 0からリストの要素数分ループ
    if i+1 in number:
        token[i+1] = words[i][:1:1]
    else:
        token[i+1] = words[i][:2:1]
print(token)
