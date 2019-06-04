import knock30

morphs = knock30.data_shape()
phrase_list = []
phrase = []
for n in range(len(morphs)):
    if morphs[n]["pos"] == "名詞":
        phrase.append(morphs[n]["surface"])
    else:
        if len(phrase) > 1:
            phrase_list.append("".join(phrase))
        phrase.clear()

print(phrase_list)
