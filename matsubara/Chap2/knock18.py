with open("hightemp.txt", "r", encoding="UTF-8") as readf:
    row = readf.readlines()
row.sort(key=lambda n:(n.split("\t")[2]), reverse=True)
for line in row:
    print(line.strip())