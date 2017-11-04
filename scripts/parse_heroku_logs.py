
import json
import re
from io import StringIO

def process_model(encoded):
    # print(encoded)
    import base64, pickle
    data = base64.b64decode(encoded)
    model = pickle.loads(data)
    print(model.__class__)
    return model.__class__

def read_file(name):
    counts = {}
    f = open(name , 'r')
    i, k = 0, 0
    for line in f:
        i = i + 1
        if(line.startswith('JSON')):
            # print(line[0:50])
            if("_parsed_content_type" not in line):
                k = k + 1
                prefix = re.sub('JSON :  ', '', line)
                prefix = re.sub("'", '"', prefix)
                io = StringIO(prefix)
                # print(io.getvalue())
                d = json.load(io)
                # print(d.keys())
                model_info = process_model(d['PickleData'])
                model = d['Name'] + "_" + str(model_info) + "_" + d['PickleData'][0:20]
                counts[model] = counts.get(model, 0) + 1
                print("LINE" , i , k, model[0:80] , counts[model])
            else:
                prefix = re.sub("^(.*)'REMOTE_ADDR'", "'REMOTE_ADDR'", line)
                prefix = re.sub("'werkzeug.server.shutdown'(.*)$", "", prefix)
                print("REMOTE_INFO" , prefix)
                
    for (k, v) in counts.items():
        print("COUNT" , k[0:80] + "..." + k[-80:] , v)


read_file('log.ws4')
