import pickle
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

with open('dataX.pkl', 'rb') as f1:
    X = pickle.load(f1)

with open('dataY.pkl', 'rb') as f2:
    y = pickle.load(f2)

lsa = TruncatedSVD(n_components=50)
lsa_result = lsa.fit(X)
X = lsa_result.transform(X)

X = np.array(X).tolist()
y = np.array(y).tolist()
X_5f = []
X_non5f = []
y_5f = []
y_non5f = []

for ele in range(len(y)):
    if y[ele] != 0:
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
f1_weighted = cross_validation.cross_val_score(clf, X, y, cv=4, scoring='f1_weighted', n_jobs=4)
print('f1_weighted:' + str(f1_weighted.mean()))

with open('lsa.pkl', 'wb') as f1:
    pickle.dump(lsa_result, f1)

with open('model.pkl', 'wb') as f2:
    pickle.dump(clf, f2)
