import json
import re

with open("england.json", "r", encoding="UTF-8") as jsonf:
    df = json.loads(jsonf.read())
    text = df["text"]
    pattern1 = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
    basic = re.findall(pattern1, text)

    new_dict = {}
    for info in basic:
        info = list(info)
        if "'" in info[1]:
            info[1] = re.sub("'", "", info[1])
        new_dict[info[0]] = info[1]

print(new_dict)
# [print(info) for info in new_info]
