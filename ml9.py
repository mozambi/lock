from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn import datasets

iris = datasets.load_iris()
print("Iris data set Loadedd")
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

for i in range(len(iris.target_names)):
    print("label:", i, "-", str(iris.target_names[i]))
classifier = KNeighborsClassifier(n_neighbors = 2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print("Results of classificatiion using K_nn with k =2")
for r in range (0, len(x_test)):
    print("Sample:", str(x_test[r]), "Actual Label:", str(y_test[r]), "Predicted_label:", str(y_pred[r]))
print("\n classification Acuuracy : ", classifier.score(x_test, y_test))
print("\n Confusion Matrix :\n", metrics.confusion_matrix(y_test, y_pred))
