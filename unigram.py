# Uni-gram model to generate sensible looking gibberish, 
# in the process of making it better
# Author: Karthik Subramanian
# Twitter / github: @yeskarthik

import random

N = 1000
sourceFile = 'boywholived.txt'
destFile = 'boywhoisgoingtolive.txt'

def getFirstWord(wordMap):
  while 1:
    firstword = random.choice(wordMap.keys())
    if firstword[0].istitle():
      return firstword

def constructWordMap(source):
  d = {} #WordMap
  with open(source, 'r') as f:
    lines = f.readlines()
    for line in lines:
      prev = None
      for word in line.split():
        if prev == None:
          prev = word
          continue
        try:
          d[prev] = list(set(d[prev] + [word]))
        except:
          d[prev] = [word]
        finally:
          prev = word
  #print d
  return d

def generateText(wordMap, destination, size):
  with open(destination, 'w') as f:
    #pick a random first word
    #firstword = random.choice(d.keys())
    firstword = getFirstWord(wordMap)
    print firstword,
    f.write(firstword)
    prev = firstword
    #pick the next word and keep picking
    for i in range(1, size):
      try:
        if prev == None:
          # If no prev word, pick a proper random first word.
          curr = getFirstWord(wordMap)
        else:
          # based on the previous word, pick the next word from the list of probables
          curr = random.choice(wordMap[prev])
        print curr,
        f.write(' ' + curr)
        prev = curr
      except:
        print '. '
        f.write('.\n')
        prev = None

wordMap = constructWordMap(sourceFile)
generateText(wordMap, destFile, N)
