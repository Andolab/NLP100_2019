import collections

with open("hightemp.txt", "r", encoding="UTF-8") as readf:
    row = readf.readlines()
col1_list = []
col1_list = [col.split("\t")[0] for col in row]
c = collections.Counter(col1_list)
[print(c) for c in c.most_common()]
