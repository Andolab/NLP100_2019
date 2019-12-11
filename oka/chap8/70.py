import random

name_pos = "rt-polaritydata/rt-polaritydata/rt-polarity.pos"
name_neg = "rt-polaritydata/rt-polaritydata/rt-polarity.neg"
text_name = "sentiment.txt"

result = []

with open(name_pos, mode="r", encoding="cp1252") as f:
    result.extend(["+1 {}".format(line.strip()) for line in f])

with open(name_neg, mode="r", encoding="cp1252") as f:
    result.extend(["-1 {}".format(line.strip()) for line in f])

random.shuffle(result)

with open(text_name, mode="w", encoding="cp1252") as f:
    print(*result, sep="\n", file=f)

pos = 0
neg = 0
with open(text_name, mode="r", encoding="cp1252") as f:
    for line in f:
        if "+1" in line:
            pos += 1
        elif "-1" in line:
            neg += 1

print(str(pos) + " " + str(neg))
