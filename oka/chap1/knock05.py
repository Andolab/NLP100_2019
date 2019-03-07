def ngram(string, number, group):
    for i in range(len(string)-number+1):
        group.add(str(string[i:i+number]))


s = "I am an NLPer"
words = s.split()
char_ngram = set()
word_ngram = set()
ngram(words, 2, word_ngram)
ngram(s.replace(" ", ""), 2, char_ngram)
print(word_ngram)
print(char_ngram)
