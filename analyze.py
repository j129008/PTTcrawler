import pickle
import numpy as np
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn.decomposition import TruncatedSVD

with open('dataX.pkl', 'rb') as f1:
    X = pickle.load(f1)

with open('dataY.pkl', 'rb') as f2:
    y = pickle.load(f2)

lsa = TruncatedSVD(n_components=100)
X = lsa.fit_transform(X)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X[:10000], y[:10000])

yPred = clf.predict(X)
print(f1_score(y[10000:], yPred[10000:], average='binary'))
