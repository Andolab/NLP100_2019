import json
import re

with open("england.json", "r", encoding="UTF-8") as jsonf:
    for line in jsonf:
        df = json.loads(line)
        for word in df["text"].split("\n"):
            pattern = r"==*\w.*=="
            section = re.search(pattern, word)
            if section is not None:
                level = section.group().count("=") // 2 - 1
                print(re.sub("=", "", section.group()), level)
