def n_gram(targetwords, n):
    n_gram = []
    for i in range(len(targetwords)-1):
        n_gram.append(targetwords[i:i+n])
    return n_gram


if __name__ == "__main__":
    words = "I am an NLPer"
    print(n_gram(words, 2))
    print(n_gram(words.split(" "), 2))
