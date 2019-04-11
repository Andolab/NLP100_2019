# 1列目の異なり
def difference(out):
    first = []
    for i in range(len(out)):
        if out[i][0] in first:
            continue
        else:
            first.append(out[i][0])
    print(first)


# ファイルの読み込み
def reading(path):
    with open(path, mode="r", encoding="utf-8") as f:
        s = f.readlines()
    elements = [elem.split() for elem in s]
    return elements


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
out = reading(path)
difference(out)
