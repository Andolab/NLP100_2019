def cipher(sentence):
    sentenceList = []
    result = ""

    for i in range(len(sentence)):
        if sentence[i].islower():
            sentenceList.insert(i, chr(219 - ord(sentence[i])))
        else:
            sentenceList.insert(i, sentence[i])

    for j in range(len(sentence)):
        result += sentenceList[j]

    return result


if __name__ == '__main__':
    sentence = "I Am An Engineer"
    print("origin sentence : " + sentence)
    cipher_sentence = cipher(sentence)
    print("cipher sentence : " + cipher_sentence)
    decode_sentence = cipher(cipher_sentence)
    print("decode sentence : " + decode_sentence)
