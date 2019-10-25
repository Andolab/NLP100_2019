def n_gram(target, n):
    result = []
    for idx in range(len(target) - n + 1):
        result.append(target[idx:idx + n])
    return result


if __name__ == '__main__':
    target = "I am an NLPer"
    words_target = target.split()
    result = n_gram(target, 2)
    print(result)
    result = n_gram(words_target, 2)
    print(result)
