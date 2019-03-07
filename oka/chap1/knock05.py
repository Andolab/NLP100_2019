def ngram(string, number):
    for i in range(len(string)-1):
        for j in range(number):
            print(string[i+j], end="")
        print(", ", end="")
    print("")


s = "I am an NLPer"
words = s.split()
ngram(words, 2)
ngram(s, 2)
