import random


def Typoglycemia(words):
    words = list(words.split())

    for k in range(len(words)):
        # 四文字以上の単語をシャッフル
        if len(words[k]) > 4:
            arr = list(words[k][1:-1])
            random.shuffle(arr)
            words[k] = words[k][0] + "".join(arr) + words[k][-1]

        words[k] += " "
    return "".join(words)


test = "I couldn\'t believe that I could actually understand what I was reading "\
       "the phenomenal power of the human mind."

print(Typoglycemia(test))
