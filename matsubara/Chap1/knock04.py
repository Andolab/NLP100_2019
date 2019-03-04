str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. "\
      "New Nations Might Also Sign Peace Security Clause. Arthur King Can."

newstr = {}
list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for k, word in enumerate(str.split()):
    if k+1 in list:
        length = 1
    else:
        length = 2
    newstr[k+1] = word[:length]

print(newstr)
