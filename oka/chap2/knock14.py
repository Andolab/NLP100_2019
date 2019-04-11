import subprocess


# 先頭のnumber行だけ出力
def head(lines, number):
    for i in range(number):
        print(lines[i])


def reading(path):
    with open(path, mode="r", encoding="utf-8") as f:
        s = f.read().splitlines()
    return s


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
out = reading(path)
print("数字を打ってください（1～24）")
number = int(input())
if 1 <= number <= 24:
    head(out, number)
else:
    print("やり直してね")
query = ["head", path, "-n", str(number)]
subprocess.call(query)
