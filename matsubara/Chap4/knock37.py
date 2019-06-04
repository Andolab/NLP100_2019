import knock30
import collections
from matplotlib import pyplot as plt
import numpy as np

morphs = knock30.data_shape()

counter = collections.Counter([m["surface"] for m in morphs])
data = counter.most_common()[0:10]

# 棒グラフの設定
label = [word[0] for word in data]
x = np.array(range(0, 10))
y = np.array([times[1] for times in data])
plt.rcParams["font.sans-serif"] = ["Yu Gothic"]
plt.title("出現頻度上位10語の推移")
plt.bar(x, y, tick_label=label, align="center")
plt.show()
