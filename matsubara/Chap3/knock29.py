import knock25
import re
import requests

endpoint = "https://en.wikipedia.org/w/api.php"

pattern1 = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
basic = knock25.get_eng_article(pattern1)
new_dict = {}
for info in basic:
    info = list(info)
    info[1] = re.sub("'|<.*>|{.*}", "", info[1])
    pattern2 = "\[+\W.*?\]+"
    if re.search(pattern2, info[1]):
        info[1] = re.sub("\[|\]", "", info[1])
    new_dict[info[0]] = info[1]
flag_img = new_dict["国旗画像"]

# 受け渡し情報
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:{}".format(flag_img),
    "iiprop": "url"
}
wikidata = requests.get(endpoint, params=params).json()
print(wikidata["query"]["pages"].popitem()[1]["imageinfo"][0]["url"])
