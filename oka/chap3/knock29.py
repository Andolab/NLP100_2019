import json
import gzip
import re
import requests
# import codecs
# from collections import OrderedDict
# import pprint


def remove_markup(text):
    text2 = re.sub(r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]", r"\1", text)
    text2 = re.sub(r"<.+?>", r"", text2)
    return re.sub(r"\'{2,5}", "", text2)


path = "C:\\Users\\16t215\\Desktop\\jawiki-country.json.gz"
with gzip.open(path, mode="rt", encoding="utf-8") as f:
    for line in f:
        data_json = json.loads(line)
        if data_json["title"] == "イギリス":
            text = data_json["text"]
            break

# 基礎情報の抜き出し
text_list = re.findall(r"基礎情報 国(.+)(?<=\n}}\n)", text, re.MULTILINE + re.DOTALL)
text_list2 = re.findall(r"\n\|(.*?) = (.*?)(?=\n\||\n}}\n)", text_list[0], re.DOTALL)
# print(text_list)
# print(text_list2)

# 辞書作り
text_dictionary = {}
for dictionary in text_list2:
    text_dictionary[dictionary[0]] = remove_markup(dictionary[1])

# 画像抜き出し
image_name = text_dictionary["国旗画像"].strip()
wiki_url = "http://en.wikipedia.org/w/api.php?"
# リクエストのパラメータ定義
params = {
    "action": "query",
    "titles": "File:{}".format(image_name),
    "prop": "imageinfo",
    "iiprop": "url",
    "format": "json"
}

# リクエスト実行
data = requests.get(wiki_url, params=params).json()

# 画像URLを取得
print(list(data["query"]["pages"].values())[0]["imageinfo"][0]["url"])
