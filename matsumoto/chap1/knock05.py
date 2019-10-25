str = "I am an NLPer"


def n_gram(str, n):
    return [str[idx:idx+n] for idx in range(len(str)-n+1)]


word_list = str.split()

print(n_gram(str, 2))
print(n_gram(word_list, 2))
