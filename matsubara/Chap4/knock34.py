import knock30

morphs = knock30.data_shape()
phrase_list = []
for n in range(len(morphs)):
    if morphs[n-1]["pos"] == "名詞" and morphs[n]["surface"] == "の" and morphs[n+1]["pos"] == "名詞":
        phrase = morphs[n-1]["surface"] + morphs[n]["surface"] + morphs[n+1]["surface"]
        phrase_list.append(phrase)

[print(phrase) for phrase in phrase_list]
