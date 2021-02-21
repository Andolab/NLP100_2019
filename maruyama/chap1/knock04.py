def ans_dict(words):
    target_counts = [1, 5, 6, 7, 8, 9, 15, 16, 19, 0]
    ans_dict = {}
    for count, word in enumerate(words.split(" "), 1):
        for target_count in target_counts:
            if target_count == count:
                ans_dict[count] = word[0]
                break
        if target_count == 0:
            ans_dict[count] = word[0:2]
    print(ans_dict)


target_words = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans_dict(target_words)
