import knock30


sentences = knock30.maping()
for sentence in sentences:
    for i in range(1, len(sentence) - 1):
        if sentence[i]["surface"] == "の" \
                and sentence[i - 1]["pos"] == "名詞" \
                and sentence[i + 1]["pos"] == "名詞":
            print(sentence[i - 1]["surface"] + "の" + sentence[i + 1]["surface"])
