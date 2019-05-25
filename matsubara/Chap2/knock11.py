# file = open('hightemp.txt', 'r', encoding='UTF-8')
# filedata = file.read()
# with as だとfile.close()を書かなくてよい
with open('hightemp.txt', 'r', encoding='UTF-8') as file:
    filedata = file.read()

# タブをスペースに置換
filedata = filedata.replace('\t', ' ')
print(filedata)

# # file = open('hightemp.txt', 'w', encoding='UTF-8')
# file.write(filedata)
with open('hightemp.txt', 'w', encoding='UTF-8') as file:
    file.write(filedata)
