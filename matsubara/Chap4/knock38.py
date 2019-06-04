import knock30
import collections
from matplotlib import pyplot as plt
import numpy as np

morphs = knock30.data_shape()

counter = collections.Counter([m["surface"] for m in morphs])
data = counter.most_common()
x = [times[1] for times in data]

# ヒストグラムの設定
freq_max = 20
plt.rcParams["font.sans-serif"] = ["Yu Gothic"]
plt.title("単語の出現頻度と種類数")
plt.xlabel("出現頻度")
plt.ylabel("種類数")
plt.xticks(range(1, freq_max+1))
plt.hist(x, range=(0, freq_max), bins=20)
plt.show()
