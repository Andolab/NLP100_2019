import re


def words_pylist(target_words):
    target_wordslist = target_words.split(" ")
    ans_words = []
    for words in target_wordslist:
        ans_words.append(len(re.sub('[,|.]', "", words)))
    print(ans_words)


words = "Now I need a drink, \
    alcoholic of course, after the heavy lectures involving quantum mechanics."
words_pylist(words)
