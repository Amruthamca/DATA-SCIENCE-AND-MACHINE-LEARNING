import pandas as pd
dataset =pd.read_csv('iris.csv')
X=dataset.iloc[:,:1]
Y=dataset.iloc[:,4]
print(X)
print(Y)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,Y_train)
Y_pred=classifier.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(Y_test,Y_pred))
print(confusion_matrix(Y_test,Y_pred))
df=pd.DataFrame({'Real_value':Y_test,'predicted_value':Y_pred})
print(df)
