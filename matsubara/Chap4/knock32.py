import knock30

morphs = knock30.data_shape()
verb_list = []
for m in morphs:
    if m["pos"] == "動詞":
        verb_list.append(m["base"])

print(verb_list)
