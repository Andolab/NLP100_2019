s = "Now I need a drink, alcoholic of course, after \
    the heavy lectures involving quantum mechanics."
words = s.split()
token = []
for i in range(0, len(words)):  # 0からリストの要素数分ループ
    token.append(len(words[i].strip(",.")))  # リストの要素の文字数をリストに格納する
print(token)
