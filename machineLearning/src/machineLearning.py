from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np


#Collect Training Data
#[weight, texture] 0=bumpy 1=smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

#0=apple 1=orange
labels = ['0','0','1','1']


#Make Classifer
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


#Make Predictions
#print clf.predict([[150,0]])


##IRIS
iris = load_iris()

test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


##Make Classifer
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#Conduct Test
print '#####TEST DATA####', test_target

#Make prediction
print '####MAKE PREDICITION####', clf.predict(test_data)


#Viz code
from sklearn.externals.six import StringIO
import pydot
from graphviz import Digraph
import pydotplus
from subprocess import check_call
#clf = clf.fit(train_data, train_target)
#tree.export_graphviz(clf,out_file='/Users/christopher.rosa/Desktop/wild/tree.dot')
#check_call(['ls','-lsa'])
#(graph,) = pydot.graph_from_dot_file('/Users/christopher.rosa/Desktop/wild/tree.dot')
#graph.write_png('/Users/christopher.rosa/Desktop/wild/tree.png')

dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph[0].write_pdf('iris.pdf')