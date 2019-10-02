import re
import nltk
from nltk.stem.porter import PorterStemmer as PS
import knock71
import pdb


def input_file(filepath: str):
    # ファイル読み込み
    with open(filepath, "r", encoding="cp1252") as f:
        text = f.read()
    return text


def stemming(words_list):
    new_words_list = []
    ps = PS()
    for words in words_list:
        new_words_list.append(ps.stem(words))
    return new_words_list


def remove_stopword_and_stemming(textset: str, stop_word: list):
    text = re.sub("[^a-z^\s]", "", textset)
    words = str.lower(text).split()
    stm_word = stemming(words)
    stm_stop_words = knock71.remove_stopword(stm_word, stop_word)
    return stm_stop_words


def pull_adj_bow(text: str, stop_word: list, dup_flag: bool):
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    stm_words = remove_stopword_and_stemming(text, stop_word)
    word_tag_list = nltk.pos_tag(stm_words)
    adj_list = []
    for word in word_tag_list:
        # if word[1] == "JJ":
        #     if dup_flag:
        #         adj_list.append(word[0])
        #     else:
        #         if word[0] not in adj_list:
        #             adj_list.append(word[0])
        adj_list.append(word[0])
    return adj_list


def adj_corpus(filepath: str, stop_word: list):
    text = input_file(filepath)
    adj_list = pull_adj_bow(text, stop_word, False)
    return adj_list


if __name__ == "__main__":
    negpath = "rt-polaritydata/rt-polarity.neg"
    pospath = "rt-polaritydata/rt-polarity.pos"
    stop_word = knock71.input_stopword()
    neg_adj = adj_corpus(negpath, stop_word)
    pos_adj = adj_corpus(pospath, stop_word)
    print(neg_adj, pos_adj)
