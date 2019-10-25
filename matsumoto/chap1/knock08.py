def cipher(str):
    result = ''
    for char in str:
        if char.isalpha():
            result += chr(219 - ord(char))
        else:
            result += char
    return result


str = input("文字列を入力してください：")
result = cipher(str)
print(result)
print(cipher(result))
