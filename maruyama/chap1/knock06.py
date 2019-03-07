from knock05 import n_gram

target1 = "paraparaparadise"
target2 = "paragraph"

target1_set = set(n_gram(target1, 2))
target2_set = set(n_gram(target2, 2))

# 和集合
print(target1_set | target2_set)
# 積集合
print(target1_set & target2_set)
# 差集合
print(target1_set - target2_set)
# seが含まれるか
print("se" in target1_set)
print("se" in target2_set)
