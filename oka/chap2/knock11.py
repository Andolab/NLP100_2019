import subprocess


path = "C:\\Users\\16t215\\Desktop\\hightemp.txt"
with open(path, mode="r", encoding="utf-8") as f:
    s = f.read()
    text = s.replace("\t", " ")
    print(text)
query = ["sed", "-e", "s/\\t/ /g", path]
subprocess.call(query)
