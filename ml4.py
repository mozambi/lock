from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,classification_report
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
model=MLPClassifier(hidden_layer_sizes=(10,),activation='relu',max_iter=1000,random_state=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("accuracy:",accuracy_score(y_test,y_pred))
print("\nClassification report:")
print(classification_report(y_test,y_pred,target_names=iris.target_names))
