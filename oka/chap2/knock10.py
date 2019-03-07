import subprocess


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
with open(path, encoding="utf-8") as f:
    s = f.readlines()
    print(len(s))
queri = ["wc", "-l", path]
subprocess.call(queri)
