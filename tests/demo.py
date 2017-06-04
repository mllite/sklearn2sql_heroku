import pickle, json, requests, base64
from sklearn import datasets 
from sklearn.ensemble import *

# get a dataset 
iris = datasets.load_iris()# or whatever dataset
# train a model on the dataset
clf = RandomForestClassifier(n_estimators=12, random_state = 1960).fit(iris.data, iris.target)

# stringify the model
b64_data = base64.b64encode(pickle.dumps(clf))
# send the model th the web service
json_data={"Name":"model1", "PickleData":b64_data , "SQLDialect":"oracle"}
r = requests.post("https://sklearn2sql.herokuapp.com/model", json=json_data)
content = r.json()
lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
print(lSQL);
