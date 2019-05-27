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
# ヒストグラムの設定
pyplot.hist(y, bins=20, range=(1, 20))
pyplot.xlim(xmin=1, xmax=20)
pyplot.grid(axis="y")
pyplot.show()
