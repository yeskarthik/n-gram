import nltk

N = 2
FILENAME = 'thirukural_corpus.txt'
OUTPUT = 'puthu_kural.txt'

with open(FILENAME, 'r') as f:
  model = nltk.model.ngram.NgramModel(N, f.read().decode('utf8').split())
  with open(OUTPUT, 'w') as o:
    o = open(OUTPUT, 'w')
    o.write(" ".join(model.generate(200)).encode('utf8'))
