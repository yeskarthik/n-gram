# Bi-gram model to generate sensible looking gibberish, 
# in the process of making it better
# Author: Karthik Subramanian
# Twitter / github: @yeskarthik

import random

N = 1000
sourceFile = 'boywholived.txt'
destFile = 'boywhoisgoingtolivetwice.txt'

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
      prev_1 = None #prev-1
      for curr in line.split():
        if prev == None and prev_1 == None:
          prev = curr
          prev_1 = None
          continue
        elif prev_1 == None:
          prev_1 = prev
          prev = curr
          continue

        try:
          d[prev_1][prev] = d[prev_1][prev] + [curr]
        except KeyError:
          d[prev_1] = {prev: [curr]}
        finally:
          prev_1 = prev
          prev = curr 
  #print d
  return d

def generateText(wordMap, destination, size):
  with open(destination, 'w') as f:
    #pick a random first word
    #firstword = random.choice(d.keys())
    firstWord = getFirstWord(wordMap)
    print firstWord,
    f.write(firstWord)
    prev_1 = firstWord
    #pick the next word and keep picking
    for i in range(1, size):
      try:
        if prev_1 == None:
          # If no prev word, pick a proper random first word.
          curr = getFirstWord(wordMap)
        else:
          # based on the previous word, pick the next word from the list of probables
          prev = random.choice(wordMap[prev_1].keys())
          curr = random.choice(wordMap[prev_1][prev])
        print prev, curr,
        f.write(' ' + prev + ' ' + curr)
        prev_1 = curr
        
      except:
        print '. '
        f.write('.\n')
        prev_1 = None

wordMap = constructWordMap(sourceFile)
generateText(wordMap, destFile, N)
