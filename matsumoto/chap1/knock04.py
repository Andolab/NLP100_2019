str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
        New Nations Might Also Sign Peace Security Clause. Arthur King Can."

first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
words = str.split()
loc = {}

for (a, b) in enumerate(words):
    if a in first_only:
        loc[b[0:1:]] = a
    else:
        loc[b[0:2:]] = a

print(loc)
