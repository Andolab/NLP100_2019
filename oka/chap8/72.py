import snowballstemmer
import stopword
from collections import Counter

stemmer = snowballstemmer.stemmer("english")
word_counter = Counter()

with open("sentiment.txt", mode="r", encoding="cp1252") as f:
    for line in f:
        for word in line[3:].split(" "):
            word = word.strip()  # 前後の空白除去

            # ストップワード除去
            if stopword.stopword(word):
                continue
            
            # ステミング
            word = stemmer.stemWord(word)
            # 条件で除去
            # if word != "!" and word != "?" and len(word) <= 1:
            if len(word) <= 1:
                continue

            # 候補に追加
            word_counter.update([word])
features = [word for word, count in word_counter.items() if count >= 7]

with open("feature.txt", mode="w", encoding="cp1252") as f:
    print(*features, sep="\n", file=f)
