import pickle
import numpy as np
from sklearn.metrics import f1_score
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

with open('dataX.pkl', 'rb') as f1:
    X = pickle.load(f1)

with open('dataY.pkl', 'rb') as f2:
    y = pickle.load(f2)

lsa = TruncatedSVD(n_components=100)
X = lsa.fit_transform(X)

X = np.array(X).tolist()
y = np.array(y).tolist()
X_5f = []
X_non5f = []
y_5f = []
y_non5f = []

for ele in range(len(y)):
    if y[ele] == 1:
        X_5f.append(X[ele])
        y_5f.append(y[ele])
    else:
        X_non5f.append(X[ele])
        y_non5f.append(y[ele])

X_train = X_non5f[:len(X_5f)] + X_5f[:]
X_train = np.array(X_train)
y_train = y_non5f[:len(y_5f)] + y_5f[:]
y_train = np.array(y_train)

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X_train, y_train)
scores = cross_validation.cross_val_score(clf, X, y, cv=5, scoring='f1', n_jobs=4)
print(scores)

# yPred = clf.predict(X)
# print(f1_score(y, yPred, average='binary'))
