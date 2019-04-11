# from itertools import groupby
from collections import Counter


# 頻度順
def frequency(out):
    out.sort()
    count = Counter(out)
    print(count)
    # result = [(k, len(list(g))) for k, g in groupby(out)]


# ファイルの読み込み
def reading(path):
    with open(path, mode="r", encoding="utf-8") as f:
        s = f.readlines()
    elements = [elem.split()[0] for elem in s]
    return elements


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
out = reading(path)
frequency(out)
