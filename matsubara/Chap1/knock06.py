def ngram(words, n):
    return list(words[i:i + n] for i in range(len(words) - n + 1))


str1 = "paraparaparadise"
str2 = "paragraph"

X = ngram(str1, 2)
Y = ngram(str2, 2)
# 集合の作成
set_x = set(X)
set_y = set(Y)

# 和集合
print(set_x | set_y)
# 積集合
print(set_x & set_y)
# 差集合
print(set_x - set_y)

# seの有無
print("集合Xに\"se\"がふくまれるか : " + str("se" in set_x))
print("集合Xに\"se\"がふくまれるか : " + str("se" in set_y))
