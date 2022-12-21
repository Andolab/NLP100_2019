import tarfile
import random


def thawing():
    # 解凍
    with tarfile.open("rt-polaritydata.tar.gz", "r:*") as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar)
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
