import random

str = "I couldn't believe that I could actually understand\
        what I was reading : the phenomenal power of the human mind ."

words = str.split()

result = []

for word in words:
    if len(word) <= 4:
        result.append(word)
    else:
        tmplist = list(word[1:-1])
        for i in range(len(tmplist)):
            k = random.randint(0, i)
            tmplist[i], tmplist[k] = tmplist[k], tmplist[i]
        result.append(word[0]+''.join(tmplist)+word[-1])

print(' '.join(result))
