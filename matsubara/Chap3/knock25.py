import json
import re


def get_eng_article(pattern: str):
    with open("england.json", "r", encoding="UTF-8") as jsonf:
        df = json.loads(jsonf.read())
    text = df["text"]
    prog = re.compile(pattern)
    return prog.findall(text)
    # return prog


if __name__ == "__main__":
    pattern = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
    basic = get_eng_article(pattern)
    print(dict(basic))
