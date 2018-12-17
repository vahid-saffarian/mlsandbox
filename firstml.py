from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [186, 86, 44], [165, 45, 37], [170, 59, 40], [187, 81, 45], [187, 100, 43]]
Y = ['male', 'female', 'female', 'male', 'female', 'female', 'male', 'male']

#clf=tree.DecisionTreeClassifier()
#clf=clf.fit(X, Y)
#prediction = clf.predict([[175, 100, 45]])

clf = MultinomialNB()
clf = clf.fit(X, Y)
prediction = clf.predict([[175, 100, 45]])
print('predicted gender is ', prediction)
