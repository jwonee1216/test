from sklearn import tree

# features = ('size', 'detail')
# detail(1='smooth', 2='bumpy')
features = [[140,1], [130,1], [150,0], [170,0]]
# result(1='apple', 2='orange')
labels = [1, 1, 0, 0]

# classifier - decision tree
clf = tree.DecisionTreeClassifier()
# 'fit' means 'get pattern'
clf = clf.fit(features, labels)
# predict using data
newdata = [[int(input()), int(input())]]
result = clf.predict(newdata)

if result == 1:
    print('apple')
else:
    print('orange')
