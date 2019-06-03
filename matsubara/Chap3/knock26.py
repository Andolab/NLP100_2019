import knock25
import re

pattern = "(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
basic = knock25.get_eng_article(pattern)
new_dict = {}
for info in basic:
    info = list(info)
    if "'" in info[1]:
        info[1] = re.sub("'", "", info[1])
    new_dict[info[0]] = info[1]

print(new_dict)
