# ファイルをN分割
def filesplit(lines, number):
    ploto = "C:\\Users\\16t215\\Desktop\\"
    limit = 24 // number
    if (24 % number != 0):
        limit += 1
    for i in range(number):
        filenumber = int(i)
        filename = "{0}split{1}.txt".format(ploto, i)
        # filename = ploto + "split" + str(filenumber) + ".txt"
        writing(filename, lines, filenumber*limit, limit)


# N分割ファイル作り
def writing(path, lines, filenumber, limit):
    with open(path, mode="w", encoding="utf-8") as f:
        f.write('\n'.join([lines[filenumber + i] for i in range(limit)]))
        # for i in range(limit):
        #    f.write(lines[filenumber + i] + "\n")


# ファイルの読み込み
def reading(path):
    with open(path, mode="r", encoding="utf-8") as f:
        s = f.read().splitlines()
    return s


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
out = reading(path)
print("数字を打ってください（1～24）")
number = int(input())
if 1 <= number <= 24:
    filesplit(out, number)
else:
    print("やり直してね")
# query = ["head", path, "-n", str(number)]
# subprocess.call(query)
