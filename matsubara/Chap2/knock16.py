import sys
import math

N = int(sys.argv[1])
with open("hightemp.txt", "r", encoding="UTF-8") as readf:
    row = readf.readlines()

for k in range(math.ceil(len(row)/N)):
    with open("split" + str(k) + ".txt", "w", encoding="UTF-8") as writef:
        writef.writelines(row[k*N:k*N+N])