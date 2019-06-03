import json
import re

with open("england.json", "r", encoding="UTF-8") as jsonf:
    df = json.loads(jsonf.read())
    text = df["text"]
    pattern1 = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
    basic = dict(re.findall(pattern1, text))
    print(basic)
