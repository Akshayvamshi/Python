from sklearn import svm
from sklearn import datasets, metrics
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC


digitsdatasets = datasets.load_digits() #Loading digits datasets
x=digitsdatasets.data #Splitt
y=digitsdatasets.target
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)  #Crossvalidation with splitting
print("Loading the LinearSVC model")
model =LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,  #Loading the model 'LinearSVC SVM'
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=0.0001,
     verbose=0)
y_pred = model.fit(x_train, y_train).predict(x_test)       #Fitting the data into the model and predicting Y with x_test values.
print("Score of the LinearSVC with data and target values:")
print(model.score(x,y))             #Printing the score of the model with x & y values.
print("Accuracy of the LinearSVC model when compared with test and prediction values:")
print(metrics.accuracy_score(y_test,y_pred))          #Printing the acuuracy of the Linear SVM model.

print("Loading the 'RBF Kernel' model")
model = svm.SVC(kernel='rbf', gamma=0.01)       #Loading the model with 'RBF kernel'.
y_pred = model.fit(x_train, y_train).predict(x_test)      #Fitting the data into the model and predicting Y with x_test values.
print("Score of the model with data and target values:")
print(model.score(x,y))              #Printing the score of the model with x & y values.
print("Accuracy of the RBF Kernel model when compared with test and prediction values:")
print(metrics.accuracy_score(y_test,y_pred))        #Printing the acuuracy of the RBF SVM model.