import json

with open("england.json", "r", encoding="UTF-8") as jsonf:
    for line in jsonf:
        df = json.loads(line)
        for word in df["text"].split("\n"):
            if "Category" in word:
                print(word)
