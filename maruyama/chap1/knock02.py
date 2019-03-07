beforewords = "パトカー"
backwords = "タクシー"
answords = [(first, second) for first, second in zip(beforewords, backwords)]
print(''.join([''.join(words) for words in answords]))
