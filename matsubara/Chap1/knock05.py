def ngram(words, n):
    return list(words[i:i + n] for i in range(len(words) - n + 1))


word = "I am a NLPer"
char = word.split()

# 単語bi-gram
word_bigram = ngram(word, 2)
print(word_bigram)

# 文字bi-gram
char_bigram = ngram(char, 2)
print(char_bigram)
