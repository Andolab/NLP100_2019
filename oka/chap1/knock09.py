import random


def typoglycemia(string):
    start = string[0]
    finish = string[len(string)-1]
    mid = [string[i] for i in range(1, len(string)-1)]
    words = start
    words += "".join(random.sample(mid, len(mid)))
    words += finish
    return words


sample = "I couldn't believe that I could actually \
    understand what I was reading : the phenomenal \
    power of the human mind ."
words = sample.split()
for i in range(len(words)):
    if len(words[i]) > 4:
        print(typoglycemia(words[i]), end=" ")
    else:
        print(words[i], end=" ")
