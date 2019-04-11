import subprocess


def writing(col, elements, number):
    tokens = [elements[i][number-1] for i in range(len(elements))]
    with open(col, mode="w", encoding="utf-8") as f:
        f.write("\n".join(tokens))


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
col1 = "C:\\Users\\16t215\\Desktop\\col1.txt"
col2 = "C:\\Users\\16t215\\Desktop\\col2.txt"
with open(path, mode="r", encoding="utf-8") as f:
    s = f.readlines()
    elements = [s[i].split() for i in range(len(s))]
    writing(col1, elements, 1)
    writing(col2, elements, 2)
query1 = ["cut", "-f", "1", path]
query2 = ["cut", "-f", "2", path]
subprocess.call(query1)
subprocess.call(query2)
