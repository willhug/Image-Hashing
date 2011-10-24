import pickle
from PIL import Image

def showAll(list):
  for imgName in list:
      img = Image.open(imgName)
      img.show()


def openImages():
  file = open('dups.obj', 'r')
  dups = pickle.load(file)
  showAll(dups[0])
  print dups[0]

openImages()
  
