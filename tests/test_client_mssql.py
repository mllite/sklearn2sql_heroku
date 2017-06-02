
import numpy as np
import pandas as pd
import sqlalchemy as sa
import pickle, json, requests, base64

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data  
Y = iris.target
# print(iris.DESCR)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
clf.fit(X, Y)


def test_ws_sql_gen(pickle_data):
    WS_URL="https://sklearn2sql.herokuapp.com/model"
    b64_data = base64.b64encode(pickle_data)
    data={"Name":"model1", "PickleData":b64_data , "SQLDialect":"mssql"}
    r = requests.post(WS_URL, json=data)
    content = r.json()
    # print(content.keys())
    # print(content)
    lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
    return lSQL;


pickle_data = pickle.dumps(clf)
lSQL = test_ws_sql_gen(pickle_data)
print(lSQL)

