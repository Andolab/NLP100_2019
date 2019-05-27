import knock30


sentences = knock30.maping()
words = []
for sentence in sentences:
    for i in range(0, len(sentence) - 1):
        while sentence[i]["pos"] == "名詞":
            words.append(sentence[i]["surface"])
            i += 1
        if len(words) > 1:
            print(words)
        words = []
