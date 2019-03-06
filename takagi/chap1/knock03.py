sentence = 'Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics.'
word = sentence.split()

for i in range(len(word)):
    konma = word[i].find(',')
    priod = word[i].find('.')
    if konma != -1:
        word[i] = word[i].replace(',', '')
    elif priod != -1:
        word[i] = word[i].replace('.', '')

wc = 0
ans = ''

for i in range(len(word)):
    wc = len(word[i])
    ans += str(wc)

print(list(ans))
