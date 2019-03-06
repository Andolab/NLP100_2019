file = open('hightemp.txt', 'r', encoding='UTF-8')
filedata = file.read()

# タブをスペースに置換
filedata = filedata.replace('\t', ' ')
print(filedata)

file = open('hightemp.txt', 'w', encoding='UTF-8')
file.write(filedata)
