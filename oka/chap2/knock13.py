import subprocess


def reading(col):
    with open(col, mode="r", encoding="utf-8") as f:
        s = f.read().splitlines()
    return s


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
col1 = "C:\\Users\\16t215\\Desktop\\col1.txt"
col2 = "C:\\Users\\16t215\\Desktop\\col2.txt"
colsum = "C:\\Users\\16t215\\Desktop\\colsum.txt"
s1 = reading(col1)
s2 = reading(col2)
sum = [s1[i] + "\t" + s2[i] for i in range(len(s1))]
with open(colsum, mode="w", encoding="utf-8") as f:
    f.write("\n".join(sum))
query = ["paste", col1, col2]
subprocess.call(query)
