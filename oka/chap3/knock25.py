import json
import gzip
import re
# import codecs
# from collections import OrderedDict
# import pprint


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
text_dictionary = dict(text_list2)
print(text_dictionary)
