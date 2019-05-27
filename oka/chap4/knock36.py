import knock30
from collections import Counter

sentences = knock30.maping()
word_count = Counter()
for line in sentences:
    word_count.update([word["surface"] for word in line])

list_word = word_count.most_common()
print(list_word)
