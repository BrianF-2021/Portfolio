# python3 -m venv env/myenv
# source env/myenv/bin/activate
# pip install flask PyMysql flask-bcrypt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn import tree


music_df = pd.read_csv('my_app/static/docs/music.csv/music.csv')
# Capital X is used for input data set
X = music_df.drop(columns=['genre'])
# A lowercase y is used for output/answer data set
y = music_df['genre']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

tree.export_graphviz(model,out_file='my_app/static/docs/music_pred.dot', feature_names=['age', 'gender'], class_names=sorted(y.unique()), label='all', rounded=True, filled=True)
# predictions = model.predict([[21,1]])
# print(predictions)

# #saving the model
# joblib.dump(model, 'my_app/static/docs/music_pred.joblib')
# #loading the model
# model = joblib.load('my_app/static/docs/music_pred.joblib')
# #checking accuracy of model
# score = accuracy_score(y_test, predictions)
# print(score)



