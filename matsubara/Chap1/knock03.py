str = 'Now I need a drink, alcoholic of course, '\
      'after the heavy lectures involving quantum mechanics.'
tmpstr = str.split()
list = []
for k in tmpstr:
    k = k.rstrip(',')
    k = k.rstrip('.')
    list.append(len(k))
print(list)
