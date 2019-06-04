import re


def data_shape():
    with open("neko.txt.mecab", "r", encoding="UTF-8") as inf:
        morphs = []
        for line in inf.readlines():
            col = re.split("[\t,]", line)
            if len(col) == 1:
                break
            mor_dict = {"surface": col[0], "base": col[-3], "pos": col[1], "pos1": col[2]}
            morphs.append(mor_dict)
    return morphs


if __name__ == "__main__":
    [print(line) for line in data_shape()]
