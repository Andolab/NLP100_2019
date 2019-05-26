import knock30
from collections import Counter
from matplotlib import pyplot


sentences = knock30.maping()
word_count = Counter()
# 頻度計算
for line in sentences:
    word_count.update([word["surface"] for word in line])

# 頻度上位10件を取得
list_word = word_count.most_common()
# print(list_word)

# y軸の値の設定
y = [list_word[i][1] for i in range(len(list_word))]
# 散布図の設定
pyplot.scatter(range(1, len(y)+1), y)
pyplot.xlim(1, len(y)+1)
pyplot.ylim(1, y[0])
# 対数グラフに変更
pyplot.xscale("log")
pyplot.yscale("log")
pyplot.grid(axis="both")
pyplot.show()
