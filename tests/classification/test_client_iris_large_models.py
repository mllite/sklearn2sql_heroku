# train all possible models on the iris dataset and generate the SQL code for each supported dialect.




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

dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite"];

for lNbEstimatorsInEnsembles in [16 , 32, 64, 128, 256, 512]:
    models = [AdaBoostClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              BaggingClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              ExtraTreesClassifier(n_estimators=lNbEstimatorsInEnsembles, max_depth=3, min_samples_leaf=15, random_state = 1960),
              GradientBoostingClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              RandomForestClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960)]
    
    for clf in models:
        print("TRAINING_MODEL" , clf.__class__.__name__, lNbEstimatorsInEnsembles)
        clf.fit(X, Y)
        pickle_data = pickle.dumps(clf)
        for dialect in dialects:
            print("GENERATING_SQL_FOR" , clf.__class__.__name__ , lNbEstimatorsInEnsembles, dialect)
            lSQL = test_ws_sql_gen(pickle_data, dialect)
            print(lSQL)

