import json
import re
import requests


endpoint = "https://en.wikipedia.org/w/api.php"

with open("england.json", "r", encoding="UTF-8") as jsonf:
    df = json.loads(jsonf.read())
    text = df["text"]
    pattern1 = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
    basic = re.findall(pattern1, text)

    new_dict = {}
    for info in basic:
        info = list(info)
        info[1] = re.sub("'|<.*>|{.*}", "", info[1])
        pattern2 = "\[+\W.*?\]+"
        if re.search(pattern2, info[1]):
            info[1] = re.sub("\[|\]", "", info[1])
        new_dict[info[0]] = info[1]
        # print(info[1])
flag_img = new_dict["国旗画像"]
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:{}".format(flag_img),
    "iiprop": "url"
}
wikidata = requests.get(endpoint, params=params).json()
print(wikidata["query"]["pages"].popitem()[1]["imageinfo"][0]["url"])
