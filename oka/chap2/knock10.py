import subprocess


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
with open(path, mode="r", encoding="utf-8") as f:
    s = f.readlines()
    print(len(s))
query = ["wc", "-l", path]
subprocess.call(query)
