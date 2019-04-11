# 降順ソート
def descending(out):
    out.sort(key=lambda x: x[2])
    out.reverse()
    print(out)


# 降順バブルソート
def des(out):
    for i in range(len(out)-1):
        for j in range(len(out)-1, i):
            if(out[j][2] > out[j-1][2]):
                out[j], out[j-1] = out[j-1], out[j]
    print(out)


# ファイルの読み込み
def reading(path):
    with open(path, mode="r", encoding="utf-8") as f:
        s = f.readlines()
    elements = [elem.split() for elem in s]
    return elements


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
out = reading(path)
descending(out)
# des(out)
# print(out)
