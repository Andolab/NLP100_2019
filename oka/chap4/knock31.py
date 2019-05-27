import knock30


sentences = knock30.maping()
for sentence in sentences:
    for word in sentence:
        if word["pos"] == "動詞":
            print(word["surface"])
