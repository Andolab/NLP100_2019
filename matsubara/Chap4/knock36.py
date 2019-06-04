import knock30
import collections

morphs = knock30.data_shape()

counter = collections.Counter([m["surface"] for m in morphs])
print(counter.most_common())
