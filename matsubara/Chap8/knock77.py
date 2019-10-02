import os
import knock71
import knock72
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


def read_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
    return words


def write_file(filepath: str, word_list: list):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(" ".join(word_list))


def bow_vector(words: list, standard_words: list):
    vector = np.zeros(len(standard_words), dtype="float32")
    for word in words:
        if word in standard_words:
            vector[standard_words.index(word)] += 1
    return vector


def input_filelines(filepath: str):
    with open(filepath, "r", encoding="cp1252") as f:
        return f.readlines()


def make_vector_and_label(sent_lines: list, adj_list: list, stop_word: list):
    sent_adj = []
    labels = []
    for line in sent_lines:
        sent_adj.append(knock72.pull_adj_bow(line, stop_word, True))
        if line[:2] == "+1":
            labels.append(1)
        elif line[:2] == "-1":
            labels.append(-1)
        else:
            continue
    vector = [bow_vector(sent, adj_list) for sent in sent_adj]
    labels = np.array(labels)
    return vector, labels


def discriminant_function(y: int, W: list, f: list):
    return 1 / (1 + np.exp(-y * np.dot(W, f)))


def my_LogisticRegression(learn_data: list, labels: list):
    time = 1
    theta = 1e-3
    N = len(learn_data[0])
    W_new = np.zeros(N)
    W_old = np.ones(N)
    loss = N
    while loss > theta and time < 200:
        W_old = W_new
        eps = 0.1 / math.sqrt(time)
        s = 0
        for f_d, y in zip(learn_data, labels):
            s = s + y * ((1 - discriminant_function(y, W_old, f_d))*f_d)
        W_new = W_old + (eps * s)
        loss = np.sqrt(np.linalg.norm(W_new-W_old, ord=2))
        time += 1
        print(loss)
    return W_new


def extract_corpus(sentpath: str, stop_word: list):
    adjpath = "adj.txt"
    if os.path.exists(adjpath):
        adj_list = read_file(adjpath)
    else:
        adj_list = knock72.adj_corpus(sentpath, stop_word)
        write_file(adjpath, adj_list)
    return adj_list


def extract_learning_data(sentpath: str, adj_list: list, stopword: list):
    direcpath = "vector_and_label/"
    witpath = "weight.npy"
    v_trainpath = direcpath + "trian_vector.npy"
    v_testpath = direcpath + "test_vector.npy"
    l_trainpath = direcpath + "trian_label.npy"
    l_testpath = direcpath + "test_label.npy"
    if os.path.exists(witpath) and os.path.exists(v_trainpath):
        W = np.load(witpath)
        v_train = np.load(v_trainpath)
        v_test = np.load(v_testpath)
        l_train = np.load(l_trainpath)
        l_test = np.load(l_testpath)
    else:
        sent_lines = input_filelines(sentpath)
        (vector, labels) = make_vector_and_label(
            sent_lines, adj_list, stop_word)
        (v_train, v_test, l_train, l_test) = \
            train_test_split(vector, labels, test_size=0.2)
        W = my_LogisticRegression(v_train, l_train)
        np.save(v_trainpath, v_train)
        np.save(v_testpath, v_test)
        np.save(l_trainpath, l_train)
        np.save(l_testpath, l_test)
        np.save(witpath, W)
    return v_train, v_test, l_train, l_test, W


def expect_label(vector: list, W: list):
    probs = []
    expects = []
    for vec in vector:
        prob = discriminant_function(1, W, vec)
        probs.append(prob)
        if prob > 0.5:
            expects.append(1)
        else:
            expects.append(-1)
    return expects, probs


def pick_word(W: list, word_list: list):
    word_dict = {}
    for word, val in zip(word_list, W):
        word_dict[val] = word
    sort_value = sorted(word_dict)
    unimp_word = [word_dict[val] for val in sort_value[:10]]
    imp_word = [word_dict[val] for val in sort_value[-1:-11:-1]]
    return imp_word, unimp_word


def output_result(filepath: str, correct_labels: list, expect_labels: list, probs: list):
    text = ""
    for correct, expect, prob in zip(correct_labels, expect_labels, probs):
        text += "{0}\t{1}\t{2}\n".format(correct, expect, prob)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def get_result(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    corrects = []
    expects = []
    probs = []
    for line in lines:
        values = line.replace("\n", "").split("\t")
        corrects.append(values[0])
        expects.append(values[1])
        probs.append(values[2])
    return corrects, expects, probs


def calc_precition(expect_labels: list, correct_labels: list):
    pre_count = 0
    for expect, correct in zip(expect_labels, correct_labels):
        if expect == correct:
            pre_count += 1
    return pre_count / len(expect_labels)


if __name__ == "__main__":
    sentpath = "sentiment.txt"
    resultpath = "result.txt"
    stop_word = knock71.input_stopword()

    # 素性抽出
    print("extract corpus")
    adj_list = extract_corpus(sentpath, stop_word)

    # 実験データ抽出
    print("extract learning data")
    (v_train, v_test, l_train, l_test, W) = extract_learning_data(sentpath, adj_list, stop_word)
    (expects, probs) = expect_label(v_test, W)
    output_result(resultpath, l_test, expects, probs)
    (corrects, expects, probs) = get_result(resultpath)
    corrects = [0 if int(lab) != 1 else 1 for lab in corrects]
    expects = [0 if int(lab) != 1 else 1 for lab in expects]
    acc = accuracy_score(corrects, expects)
    pre = precision_score(corrects, expects)
    rec = recall_score(corrects, expects)
    f1 = f1_score(corrects, expects)
    print("正解率:{0}, 適合率:{1}, 再現率:{2}, F値:{3}".format(acc, pre, rec, f1))
