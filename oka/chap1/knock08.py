def cipher(string):
    word = ""
    for i in range(len(string)):
        if "a" <= string[i] <= "z":
            word += chr(219 - ord(string[i]))
        else:
            word += string[i]
    return word


print(cipher("AbCd"))
print(cipher(cipher("AbCd")))
