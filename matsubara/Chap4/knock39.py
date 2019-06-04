import knock30
import collections
from matplotlib import pyplot as plt
import numpy as np


def set_rank(data: list):
    num = 1
    rank = []
    for info, k in zip(data, range(len(data))):
        # 最終要素のとき
        if k > len(data)-2:
            if info[1] is not data[k-1][1]:
                num = k+1
        else:
            if info[1] is not data[k+1][1]:
                num = k+1
        rank.append(num)
    return rank


morphs = knock30.data_shape()
counter = collections.Counter([m["surface"] for m in morphs])
data = counter.most_common()

x = np.array([times[1] for times in data])
y = np.array(set_rank(data))

# 両対数グラフの設定
plt.rcParams["font.sans-serif"] = ["Yu Gothic"]
plt.title("単語の出現頻度と順位")
plt.xlabel("順位")
plt.ylabel("出現頻度")
plt.plot(x, y, "bo")
plt.xscale("log")
plt.yscale("log")
plt.show()
