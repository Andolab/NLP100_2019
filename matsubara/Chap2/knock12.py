text1 = ""
text2 = ""

with open("hightemp.txt", "r", encoding="UTF-8") as readfile:
    for line in readfile.readlines():
        cols = line.split("\t")
        text1 += cols[0] + "\n"
        text2 += cols[1] + "\n"

with open("col1.txt", "w", encoding="utf-8") as f1:
    f1.write(text1)

with open("col2.txt", "w", encoding="utf-8") as f2:
    f2.write(text2)
