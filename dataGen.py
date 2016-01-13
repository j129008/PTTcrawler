import json
import jieba
import jieba.analyse
import numpy as np
import pickle

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

with open('dataX.pkl', 'wb') as f0:
    pickle.dump(X, f0)

with open('dataY.pkl', 'wb') as f1:
    pickle.dump(y, f1)

