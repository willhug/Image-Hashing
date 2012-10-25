from PIL import Image
from PIL import ImageStat
import glob, pickle



def hashImage(img):
  image = Image.open(img)

  resized = image.resize([8,8]) 
  #resized.show()
  
  grey = resized.convert("L")
  #grey.show()

  stat = ImageStat.Stat(grey)
  mean =  stat.mean
  #print mean[0]
  meanVal = mean[0]
  
  bitString = ""

  for i in range(8):
    for j in range(8):
      if grey.getpixel((i,j)) > meanVal:
        bitString =  bitString + "0"
      else:
        bitString = bitString + "1"

  #print bitString
  
  hash =  int(bitString, 2)
  

  return hash

#print "0x%x" % hashImage("test2.jpg")

def showAll(list):
  for imgName in list:
    img = Image.open(imgName)
    img.show()

def runHashInDir(dir):
  dict = {}
  dups = 0
  print "STARTING TO GATHER HASHES"
  for image in glob.glob(dir + "*.jpg"):
    try:
      hash = hashImage(image)
      if hash in dict:
        current = [image]
        current.extend(dict[hash])
        dict[hash] = current
        image.save('dups/'+current)
        print "DUPLICATE"
        dups = dups + 1
      else:
        value = [image]
        image.save('newImages/'+value)
        dict[hash] = value
    except:
      pass

  file = open("dict.obj", 'w')
  pickle.dump(dict, file)
  print dict
  
  print "SHOWING DUPLICATES"
  #for values in dict.values():
  #  if values is not None:  
  #    if(len(values) > 1):
  #        print values
  #        showAll(values)
  #print "THERE ARE " + dups + " DUPLICATES"

runHashInDir("/Users/willhughes/Dropbox/Backgrounds/")
