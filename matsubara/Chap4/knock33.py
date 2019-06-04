import knock30

morphs = knock30.data_shape()
noun_list = []
for m in morphs:
    if m["pos"] == "名詞" and m["pos1"] == "サ変接続":
        noun_list.append(m["surface"])

[print(noun) for noun in noun_list]
