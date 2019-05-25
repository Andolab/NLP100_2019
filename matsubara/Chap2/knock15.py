import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r", encoding="UTF-8") as f:
    row = f.readlines()
    k = 1
    while k in range(N+1):
        print(row[-k].strip())
        k += 1
        if k > len(row):
            break