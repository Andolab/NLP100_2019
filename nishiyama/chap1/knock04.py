word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word = word.replace(',', '').replace('.', '')
word = word.split()
word_dict = {}

for i, x in enumerate(word, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        word_dict[x[:1]] = i
    else:
        word_dict[x[:2]] = i
print(word_dict.items())
