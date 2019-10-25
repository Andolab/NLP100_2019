word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word = word.replace(',', '').replace('.', '')
word = word.split()
num_word = [len(x) for x in word]
print(word)
print(num_word)
