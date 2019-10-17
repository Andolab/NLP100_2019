def random_sentence(word):
    charList = []
    newList = []
    result = ""

    for i in range(0, len(word)):
        charList.insert(i, word[i])
    wordlen = len(charList)-1
    newList.insert(wordlen, charList[wordlen])
    charList.pop()

    newList.insert(0, charList[0])
    charList.pop(0)

    charList = charList[::-1]
    for ii in range(0, len(charList)):
        newList.insert(ii+1, charList[ii])
    for iii in range(0, len(newList)):
        result += newList[iii]

    return result


if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    sentenceList = sentence.split()
    results = ""
    for i in sentenceList:
        if len(i) >= 4:
            i = random_sentence(i)
        results += i + ' '
    print(results)
