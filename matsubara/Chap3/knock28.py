import knock25
import re

pattern1 = r"(?<=\|)(.*?)\s=\s(.*?)(?=\\n\||\\n}}\\n)"
basic = knock25.get_eng_article(pattern1)
new_dict = {}
for info in basic:
    info = list(info)
    info[1] = re.sub(r"'|<.*>|{.*}", "", info[1])
    pattern2 = r"\[+\W.*?\]+"
    if re.search(pattern2, info[1]):
        info[1] = re.sub(r"\[|\]", "", info[1])
    new_dict[info[0]] = info[1]

print(new_dict)
