with open("hightemp.txt", "r", encoding="UTF-8") as readf:
    row = readf.readlines()
col1_list = []
for col in row:
    c = col.split("\t")[0]
    if c in col1_list:
        continue
    else:
        col1_list.append(c)
print("\n".join(col1_list))