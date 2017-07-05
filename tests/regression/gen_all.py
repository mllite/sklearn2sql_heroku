import os
from sklearn2sql_heroku.tests.regression import generic as reg_gen

def createDirIfNeeded(dirname):
    try:
        os.makedirs(dirname);
    except:
        pass



def create_script(model, ds, dialect):
    print("GENERATING_MODEL" , model, ds, dialect);
    dirname = "tests/regression/" + str(ds) ;
    print(dirname);
    createDirIfNeeded(dirname);
    filename = dirname + "/ws_" + ds + "_" + model + "_" + dialect + "_code_gen.py";
    file = open(filename, "w");
    print("WRTITING_FILE" , filename);
    file.write("from sklearn2sql_heroku.tests.regression import generic as reg_gen\n");
    file.write("\n\n");
    args = "\"" + model + "\" , \"" + ds + "\" , \"" + dialect + "\"";
    file.write("reg_gen.test_model(" + args + ")\n");
    file.close();

models = reg_gen.get_models()
datasets = reg_gen.get_datasets()

dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite"];

for model in models.keys():
    for ds in datasets.keys():
        for dialect in dialects:
            create_script(model , ds, dialect)

