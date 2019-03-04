panda = "パトカー"
taxy = "タクシー"  # タクシーの綴りが間違ってるのはネタです
string = ""
for i in range(0, 5):  # 0から5まで繰り返す
    string += panda[i::4]  # i番目の文字から4文字飛ばしで付け足す
    string += taxy[i::4]  # i番目の文字から4文字飛ばしで付け足す
print(string)
