import json
import jieba
import jieba.analyse
import numpy as np
import pickle
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn.decomposition import TruncatedSVD

jieba.analyse.set_stop_words("./stopWords.txt")
jieba.load_userdict("./pttDict.txt")
feature = open("./feature","r")

with open('./data.json') as data_file:
    data = json.load(data_file)

instance = {}
genData = []
x = []
y = []

featureList = []

for ele in feature:
    featureList.append(ele.strip())

with open('feature.pkl', 'wb') as f0:
    pickle.dump(featureList, f0)

for post in data:
    ans = 0
    for ele in featureList:
        instance[ele] = 0

    for push in post['g_推文']:
        if ("五楼" or "5F" or "5f") in post['g_推文'][push]['留言內容']:
            ans = 1
    y.append(ans)

    content = post['f_內文']
    for ele in featureList:
        if ele in content:
            instance[ele] = 1

    term = []
    for ele in featureList:
        term.append(instance[ele])
    x.append(term)

X = np.array(x)
y = np.array(y)

lsa = TruncatedSVD(n_components=100)
lsa_result = lsa.fit(X)
with open('lsa.pkl', 'wb') as f1:
    pickle.dump(lsa_result, f1)
"""
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
with open('model.pkl', 'wb') as f2:
    pickle.dump(clf, f2)

"""
