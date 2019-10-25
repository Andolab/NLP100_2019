str = "Now I need a drink, alcoholic of course,\
        after the heavy lectures involving quantum mechanics."
words = str.split()
list = []

for word in words:
    ct = 0
    for char in word:
        if char.isalpha():
            ct += 1
    list.append(ct)

print(list)
