import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r", encoding="UTF-8") as f:
    for row, k in zip(f.readlines(), range(N)):
        print(row.strip())