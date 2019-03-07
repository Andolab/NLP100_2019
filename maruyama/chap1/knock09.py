import random


def random_change(target):
    target_list = target.split(' ')
    ans = []
    for word in target_list:
        if len(word) <= 4:
            ans.append(word)
        else:
            lead = word[0]
            center = word[1:-1]
            tail = word[-1]
            ans.append(lead+''.join(random.sample(center, len(center)))+tail)
    return " ".join(ans)


texts = "I couldn't believe that \
I could actually understand what \
I was reading : the phenomenal power of the human mind ."
print(random_change(texts))
