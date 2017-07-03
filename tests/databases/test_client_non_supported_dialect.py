
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
    b64_data = base64.b64encode(pickle_data).decode('utf-8')
    data={"Name":"model1", "PickleData":b64_data , "SQLDialect":"sybase"}    
    r = requests.post(WS_URL, json=data)
    print(r.__dict__.keys())
    print("STATUS_CODE", r.status_code)
    r.raise_for_status()
    content = r.json()
    # print(content.keys())
    # print(content)
    lSQL = content["model"]["SQLGenrationResult"][0]["SQL"]
    return lSQL;


pickle_data = pickle.dumps(clf)

try:
    lSQL = test_ws_sql_gen(pickle_data)
    print(lSQL)
    raise Exception("SHOULD_HAVE_FAIlED")
except Exception as e:
    print(str(e))
    if(str(e).startswith('500 Server Error')):
        pass
    else:
        raise Exception("SHOULD_HAVE_FAIlED")
        

