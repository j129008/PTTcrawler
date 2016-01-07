import json
import sys
import jieba
import jieba.analyse
import numpy as np
import pickle
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn.decomposition import TruncatedSVD
import opencc

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")

instance = {}
genData = []
x = []
y = []

featureList = []

with open('feature.pkl', 'rb') as f0:
    featureList = pickle.load(f0)

for ele in featureList:
    instance[ele] = 0

content = sys.argv[1]
content = opencc.convert(content)
for ele in featureList:
    if ele in content:
        instance[ele] = 1

term = []
for ele in featureList:
    term.append(instance[ele])
x.append(term)

X = np.array(x)

with open('lsa.pkl', 'rb') as f1:
    lsa = pickle.load(f1)
X = lsa.transform(X)

with open('model.pkl', 'rb') as f2:
    clf = pickle.load(f2)

yPred = clf.predict(X)
print(yPred)

