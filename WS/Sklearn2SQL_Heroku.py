
from __future__ import absolute_import

from flask import Flask, redirect, request #import objects from the Flask model
import os, platform
import requests, json

app = Flask(__name__)
sklearn2sql_uri = os.environ.get("SKLEARN2SQL_URI", "http://c:1888")


def get_post_response(request1):
    # request1 = request
    # print(request1.json)
    r = requests.post(sklearn2sql_uri + "/model", json=request1.json)
    # print("JSON", r.json())
    response = app.response_class(
        response=json.dumps(r.json()),
        status=200,
        mimetype='application/json'
    )
    # json.dumps(data)
    return response


@app.route('/', methods=['GET'])
def test():
    return redirect(sklearn2sql_uri, code=307)

@app.route('/models', methods=['GET'])
def returnAllModels():
    return redirect(sklearn2sql_uri, code=307)



@app.route('/model/<string:name>', methods=['GET'])
def returnOneModel(name):
    return redirect(sklearn2sql_uri + "/model/" + name, code=307)


# POST requests

@app.route('/model', methods=['POST'])
def addOneModel():
    # return redirect(sklearn2sql_uri + "/model", code=307)
    return get_post_response(request)

# PUT requests 

if __name__ == '__main__':
    print(platform.platform())
    print(platform.uname())
    print(platform.processor())
    print(platform.python_implementation(), platform.python_version());
    print(os.environ);
    port = int(os.environ.get("PORT", 1888))
    app.run(host='0.0.0.0', port=port, debug=True)
