import json
import gzip
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
text_list = text.split("\n")
for lines in text_list:
    if "Category" in lines:
        print(lines)
