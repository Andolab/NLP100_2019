def ngram(string, number, group):
    for i in range(len(string)-number+1):
        group.add(string[i:i+number])


# groupの中にstringが含まれているかの判定
def contain(group, string):
    if string in group:
        print("あります。")
    else:
        print("ありません。")


s1 = "paraparaparadise"
s2 = "paragraph"
X = set()
Y = set()
ngram(s1, 2, X)
ngram(s2, 2, Y)
print(X | Y)  # 和集合
print(X & Y)  # 積集合
print(X - Y)  # 差集合
print("Xの中にseは", end="")
contain(X, "se")
print("Yの中にseは", end="")
contain(Y, "se")
