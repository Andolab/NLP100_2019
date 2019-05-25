readfile = open('hightemp.txt', 'r', encoding='UTF-8')
rowcount = readfile.readlines()
print(len(rowcount))
