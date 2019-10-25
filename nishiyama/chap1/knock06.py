def n_gram(target, n):
    result = []
    target = target.replace(' ', '')
    for idx in range(len(target) - n + 1):
        result.append(target[idx:idx + n])
    return result


if __name__ == '__main__':
    target1 = "paraparaparadise"
    target2 = "paragraph"
    X = n_gram(target1, 2)
    Y = n_gram(target2, 2)

    X = set(X)
    Y = set(Y)

    print(X)
    print(Y)

    print("和集合")
    print(X.union(Y))
    print("差集合")
    print(X.difference(Y))
    print("積集合")
    print(X.intersection(Y))

    print("se" in X)
    print("se" in Y)
