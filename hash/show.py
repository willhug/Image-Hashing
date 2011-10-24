import pickle

def getDups():
  rfile = open("dict.obj", 'r')
  dict = pickle.load(rfile)

  dups = []

  for values in dict.values():
    if len(values) > 1:
      dups.append(values)
      print values

  print dups
  print len(dups)
  
  file = open("dups.obj", 'w')
  pickle.dump(dups, file)

getDups()
