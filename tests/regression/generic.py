from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.neural_network import *
from sklearn.ensemble import *
from sklearn.dummy import *

def get_human_friendly_name(model):
    if(hasattr(model , 'kernel')):
        lkernel = model.kernel
        return str(model.__class__.__name__) + "_" + str(lkernel)
    return str(model.__class__.__name__);


def get_models():

    lNbEstimatorsInEnsembles = 12
    
    models=[DecisionTreeRegressor(max_depth=5, random_state = 1960) ,
            AdaBoostRegressor(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
            GradientBoostingRegressor(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
            SGDRegressor(random_state = 1960),
            RandomForestRegressor(n_estimators=lNbEstimatorsInEnsembles, random_state = 1960),
            Ridge(random_state = 1960),
            SVR(max_iter=200, kernel='linear'),
            SVR(max_iter=400, kernel='poly'),
            SVR(max_iter=200, kernel='rbf'),
            MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 5), random_state=1960)]

    tested_regressors = {};
    for (i, reg) in enumerate(models) :
        name = get_human_friendly_name(reg);
        tested_regressors[name] = reg;

    return tested_regressors


def get_datasets():
    from sklearn import datasets

    gDatasets = {};
    gDatasets["diabetes"] = datasets.load_diabetes()
    gDatasets["boston"] = datasets.load_boston()
    gDatasets["freidman1"] = datasets.make_friedman1(random_state=1960)
    gDatasets["freidman2"] = datasets.make_friedman2(random_state=1960)
    gDatasets["freidman3"] = datasets.make_friedman3(random_state=1960)
    gDatasets["RandomReg_10"] = datasets.make_regression(n_features=10, n_informative=4, random_state=1960);
    gDatasets["RandomReg_100"] = datasets.make_regression(n_features=100, n_informative=10, random_state=1960);
    gDatasets["RandomReg_500"] = datasets.make_regression(n_features=500, n_informative=50, random_state=1960);

    return gDatasets;

def test_ws_sql_gen(pickle_data, dialect):
    import pickle, json, requests, base64
    WS_URL="https://sklearn2sql.herokuapp.com/model"
    # WS_URL="http://localhost:1888/model"
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
    dialects = ["db2", "mssql", "mysql", "oracle", "postgresql", "sqlite"];
    return dialects

def serialize_model(model_name , dataset_name):
    import pickle, json, requests, base64
    import os.path
    import sklearn 
    lVersion = sklearn.__version__;
    lCacheName = "tests/pickle_cache/sklreg_" + lVersion + "_" + dataset_name + "_" + model_name + ".pickle"
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
