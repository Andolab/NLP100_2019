# 暗号複合関数
def cipher(string):
    newstr = ""
    for k in string:
        if k.islower():
            newstr += chr(219 - ord(k))
        else:
            newstr += k
    return newstr


str1 = input("文字列入力 : ")

# 暗号化
cryptogram = cipher(str1)
print(cryptogram)

# 複合化
decryptogram = cipher(cryptogram)
print(decryptogram)

# 結果
if decryptogram == str1:
    print("result : True")
else:
    print("result : False")
