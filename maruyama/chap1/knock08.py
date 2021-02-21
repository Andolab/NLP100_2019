import re


def cipher(target):
    ans = []
    for c in target:
        ans.append(re.sub("[a-z]", chr(219-ord(c)) if c.islower() else c, c))
    return "".join(ans)


target = input('入力:')
encry = cipher(target)
print("暗号化:"+encry)
print("複合化:"+cipher(encry))
