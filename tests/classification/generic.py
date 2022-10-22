from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.neural_network import *
from sklearn.ensemble import *
from sklearn.dummy import *

import xgboost as xgb
import lightgbm as lgb

def get_human_friendly_name(model):
    if(hasattr(model , 'kernel')):
        lkernel = model.kernel
        return str(model.__class__.__name__) + "_" + str(lkernel)
    return str(model.__class__.__name__);

import os

def make_dir(full_path):
    try:
        os.makedirs(full_path)
    except:
        pass
    
def get_models():

    lNbEstimatorsInEnsembles = 12
    
    models = [DecisionTreeClassifier(max_depth=5, random_state = 1960) ,
              DummyClassifier(),
              AdaBoostClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              GradientBoostingClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              SGDClassifier( random_state = 1960),
              LogisticRegression( random_state = 1960),
              RandomForestClassifier(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
              GaussianNB(),
              SVC(max_iter=200, probability=True, kernel='linear', decision_function_shape='ovr'),
              SVC(max_iter=400, probability=True, kernel='poly', decision_function_shape='ovr'),
              SVC(max_iter=200, probability=True, kernel='rbf', decision_function_shape='ovr'),
              MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 5), random_state=1960),
              RidgeClassifier(random_state = 1960),
              xgb.XGBClassifier(n_estimators=10, nthread=1, min_child_weight=10, max_depth=3, seed=1960),
              SVC(max_iter=200, probability=True, kernel='sigmoid', decision_function_shape='ovr'),
              lgb.LGBMClassifier(num_leaves=40, learning_rate=0.05, n_estimators=10)]
    
    tested_classifiers = {};
    for (i, clf) in enumerate(models) :
        name = get_human_friendly_name(clf);
        tested_classifiers[name] = clf;

    return tested_classifiers


def get_datasets():
    from sklearn import datasets

    gDatasets = {};
    gDatasets["iris"] = datasets.load_iris()
    gDatasets["digits"] = datasets.load_digits()
    gDatasets["BreastCancer"] = datasets.load_breast_cancer();
    # gDatasets["kddcup99"] = datasets.fetch_kddcup99();
    gDatasets["BinaryClass_10"] = datasets.make_classification(n_classes=2, n_features=10, random_state=1960);
    gDatasets["FourClass_10"] = datasets.make_classification(n_classes=4, n_features=10, n_informative=4, random_state=1960);
    gDatasets["BinaryClass_100"] = datasets.make_classification(n_classes=2, n_features=100, random_state=1960);
    gDatasets["FourClass_100"] = datasets.make_classification(n_classes=4, n_informative=50, n_features=100, random_state=1960);
    gDatasets["BinaryClass_500"] = datasets.make_classification(n_classes=2, n_features=500, random_state=1960);
    gDatasets["FourClass_500"] = datasets.make_classification(n_classes=4, n_informative=100, n_features=500, random_state=1960);
    return gDatasets;

def test_ws_sql_gen(pickle_data, dialect):
    import pickle, json, requests, base64
    # WS_URL="https://sklearn2sql.herokuapp.com/model"
    WS_URL="http://localhost:1888/model"
    b64_data = base64.b64encode(pickle_data).decode('utf-8')
    data={"Name":"model1", "PickleData":b64_data , "SQLDialect":dialect}
    r = requests.post(WS_URL, json=data)
    print(str(r))
    try:
        content = r.json()
        # print(content.keys())
        # print(content)
        lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
        return lSQL;
    except Exception as e:
        print("FAILURE_WITH_EXCEPTION" , str(e))
        print("WS_RESPONSE_START\n")
        print(str(r))
        print("WS_RESPONSE_END\n")
        return None

def get_known_dialects():
    dialects = ["db2", "mssql", "mysql", "oracle", "postgresql", "sqlite", "duckdb"];
    return dialects

def serialize_model(model_name , dataset_name):
    import pickle, json, requests, base64
    import os.path
    import sklearn 
    lVersion = sklearn.__version__;
    lDir =  "/tmp/pickle_cache/classification/" + dataset_name
    make_dir(lDir)
    lCacheName = lDir + "/sklclass_" + lVersion + "_" + dataset_name + "_" + model_name + ".pickle"
    if(os.path.exists(lCacheName)):
        cache_file = open(lCacheName, "rb");
        pickle_data = cache_file.read()
        return pickle_data
    models = get_models()
    clf = models[model_name]
    datasets = get_datasets();
    ds = datasets[dataset_name]
    (X ,y) = (None, None)
    if(isinstance(ds, (list, tuple))):
        (X, y) = (ds[0], ds[1])
    else:
        (X ,y) = (ds.data , ds.target)

    print("TRAINING_MODEL" , model_name , dataset_name)
    clf.fit(X, y)
    pickle_data = pickle.dumps(clf)
    cache_file = open(lCacheName, "wb");
    cache_file.write(pickle_data)
    cache_file.close()
    return pickle_data

def test_model(model_name , dataset_name, dialect):
    pickle_data = serialize_model(model_name , dataset_name)
    print("GENERATING_SQL_FOR" , model_name , dataset_name, dialect)
    lSQL = test_ws_sql_gen(pickle_data, dialect)
    print(lSQL)
