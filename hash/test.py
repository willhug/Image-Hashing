dict = {}
test = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]

for i in test:
  if i in dict:
    cur = [i]
    cur.extend(dict[i])
    print cur
    dict[i] = cur 
  else:
    value = [i]
    dict[i] = value

print dict
