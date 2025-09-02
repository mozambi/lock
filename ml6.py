import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score
df=pd.read_csv("document.csv")
texts=df["text"].values
labels=df["label"].values
Vectorizer=CountVectorizer()
X=Vectorizer.fit_transform(texts)
X_train,X_test,y_train,y_test=train_test_split(X,labels,test_size=0.3,random_state=42)
model=MultinomialNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred,pos_label="positive")
recall=recall_score(y_test,y_pred,pos_label="positive")
print("test results:")
for texts,true_label,pred_label in zip(Vectorizer.inverse_transform(X_test),y_test,y_pred):
    print(f"text:{' '.join(texts)}|True:{true_label}|predicted:{pred_label}")
print("\n metrics:")
print(f"accuracy:{accuracy:.2f}")
print(f"precision:{precision:.2f}")
print(f"recall:{recall:.2f}")
