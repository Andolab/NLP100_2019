def maping():
    with open("neko.txt.mecab", encoding="utf-8") as f:
        lines = f.readlines()

    contents = []
    for line in lines:
        elements = line.split("\t")
        if (len(elements) < 2):
            continue
        ex_elements = elements[1].split(",")

        content = {
            "surface": elements[0],
            "base": ex_elements[6],
            "pos": ex_elements[0],
            "pos1": ex_elements[1]
        }
        contents.append(content)

        if ex_elements[1] == "句点":
            yield contents
            contents = []


if __name__ == "__main__":
    sentences = maping()
    for sentence in sentences:
        print(sentence)
