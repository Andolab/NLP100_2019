import tarfile
import random


def thawing():
    # 解凍
    with tarfile.open("rt-polaritydata.tar.gz", "r:*") as tar:
        tar.extractall()
        tar = list(tar)
        negfile = tar[1].name
        posfile = tar[2].name
    return negfile, posfile


def input_neg_pos(negfile, posfile):
    # ファイル読み込み
    with open(negfile, "r", encoding="cp1252") as negf,\
            open(posfile, "r", encoding="cp1252") as posf:
        neg_lines = negf.readlines()
        pos_lines = posf.readlines()

    return neg_lines, pos_lines


def count_neg_pos(filepath: str):
    with open(filepath, "r", encoding="cp1252") as inf:
        lines = inf.readlines()
    pos_count = 0
    neg_count = 0
    for l in lines:
        if "+1" in l:
            pos_count += 1
        elif "-1" in l:
            neg_count += 1
    print("pos: {0}, neg: {1}".format(pos_count, neg_count))


if __name__ == "__main__":
    negfile, posfile = thawing()
    neg_lines, pos_lines = input_neg_pos(negfile, posfile)

    new_pos_lines = ["+1 " + line for line in pos_lines]
    new_neg_lines = ["-1 " + line for line in neg_lines]
    new_lines = new_pos_lines + new_neg_lines
    random.shuffle(new_lines)
    filepath = "sentiment.txt"
    with open(filepath, "w", encoding="cp1252") as outf:
        outf.writelines(new_lines)

    count_neg_pos(filepath)
