import knock30


sentences = knock30.maping()
for sentence in sentences:
    for word in sentence:
        if word["pos"] == "名詞" and word["pos1"] == "サ変接続":
            print(word["surface"])
