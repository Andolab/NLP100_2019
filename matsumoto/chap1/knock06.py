str1 = "paraparaparadise"
str2 = "paragraph"


def n_gram(str, n):
    return [str[idx:idx+n] for idx in range(len(str)-n+1)]


set1 = set(n_gram(str1, 2))
set2 = set(n_gram(str2, 2))

print(set1)
print(set2)
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
if 'se' in set1:
    print("se はXに含まれます")
if 'se' in set2:
    print("se はYに含まれます")
