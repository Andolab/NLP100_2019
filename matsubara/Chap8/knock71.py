def input_stopword():
    with open("stopword.txt", "r", encoding="cp1252") as f:
        stop_list = [stop.replace("\n", "") for stop in f.readlines()]
    return stop_list


def check_stword(word: str, stop_list: list):
    return word in stop_list


def remove_stopword(word_list: list, stop_word: list):
    new_words = []
    for word in word_list:
        low_word = word.lower()
        if not check_stword(low_word, stop_word):
            new_words.append(word)
    return new_words


if __name__ == "__main__":
    stop_list = input_stopword()
    word_list = ["I", "am", "champion"]
    new_words = remove_stopword(word_list, stop_list)
    print(new_words)
