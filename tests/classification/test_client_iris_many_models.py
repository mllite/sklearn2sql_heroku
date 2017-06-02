# train all possible models on the iris dataset and generate the SQL code for each supported dialect.

import numpy as np
import pandas as pd
import sqlalchemy as sa
import pickle, json, requests, base64

from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.neural_network import *
from sklearn.ensemble import *
from sklearn.dummy import *
from sklearn import datasets
from sklearn import datasets

def test_ws_sql_gen(pickle_data, dialect):
    WS_URL="https://sklearn2sql.herokuapp.com/model"
    b64_data = base64.b64encode(pickle_data)
    data={"Name":"model1", "PickleData":b64_data , "SQLDialect":dialect}
    r = requests.post(WS_URL, json=data)
    content = r.json()
    # print(content.keys())
    # print(content)
    lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
    return lSQL;


iris = datasets.load_iris()
X = iris.data  
Y = iris.target
# print(iris.DESCR)

lNbEstimatorsInEnsembles = 12

models=[DecisionTreeClassifier(max_depth=5, random_state = 1960) ,
        AdaBoostClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
        GradientBoostingClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
        SGDClassifier( random_state = 1960),
        LogisticRegression( random_state = 1960),
        RandomForestClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
        GaussianNB(),
        SVC(max_iter=200, probability=True, kernel='linear'),
        SVC(max_iter=400, probability=True, kernel='poly'),
        SVC(max_iter=200, probability=True, kernel='rbf'),
        MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 5), random_state=1960),
        RidgeClassifier(random_state = 1960)]


dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite"];

for clf in models:
    print("TRAINING_MODEL" , clf.__class__.__name__)
    clf.fit(X, Y)
    pickle_data = pickle.dumps(clf)
    for dialect in dialects:
        print("GEENERATING_SQL_FOR" , clf.__class__.__name__ , dialect)
        lSQL = test_ws_sql_gen(pickle_data, dialect)
        print(lSQL)

