import json
import collections as cl
import gzip

# mode=rt: text形式として読み出す
# 1行1記事のため，1行ずつ読み出す必要がある
with gzip.open("jawiki-country.json.gz", "rt", encoding="UTF-8") as jsonf,\
        open("england.json", "w", encoding="UTF-8") as outf:
    for line in jsonf:
        df = json.loads(line)
        if df["title"] == "イギリス":
            ys = cl.OrderedDict()
            ys["text"] = df["text"]
            json.dump(ys, outf, ensure_ascii=False)
            # json.dump(ys, outf)
            break
