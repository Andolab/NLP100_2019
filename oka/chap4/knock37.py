import knock30
from collections import Counter
from matplotlib import pyplot, rcParams


sentences = knock30.maping()
word_count = Counter()
# 頻度計算
for line in sentences:
    word_count.update([word["surface"] for word in line])

# 頻度上位10件を取得
list_word = word_count.most_common(10)
print(list_word)

# x, y軸の値の設定
x = []
y = []
for i in range(10):
    x.append(list_word[i][0])
    y.append(list_word[i][1])
# 棒グラフの設定
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Yu Gothic"]
pyplot.bar(range(0, 10), y, align="center")
pyplot.xticks(range(0, 10), x)
pyplot.grid(axis="y")
pyplot.show()
