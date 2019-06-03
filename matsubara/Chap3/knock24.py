import json
import re

with open("england.json", "r", encoding="UTF-8") as jsonf:
    for line in jsonf:
        df = json.loads(line)
for word in df["text"].split("\n"):
    pattern = "(?<=File:|ファイル:).*?(?=\|)"
    filename = re.search(pattern, word)
    if filename is not None:
        print(filename.group())
