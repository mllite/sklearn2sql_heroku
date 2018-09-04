import os

def createDirIfNeeded(dirname):
    try:
        os.makedirs(dirname);
    except:
        pass



def create_script(model, ds, dialect):
    print("GENERATING_MODEL" , model, ds, dialect);
    dirname = "tests/caret/regression/" + str(ds) ;
    print(dirname);
    createDirIfNeeded(dirname);
    filename = dirname + "/ws_" + ds + "_" + model + "_" + dialect + "_code_gen.R";
    file = open(filename, "w");
    print("WRTITING_FILE" , filename);
    file.write('source("tests/caret/regression/generic.R")\n');
    file.write("\n\n");
    args = "\"" + model + "\" , \"" + ds + "\" , \"" + dialect + "\"";
    file.write("test_caret_model(" + args + ")\n");
    file.close();

models = ["rpart" , "ctree"]
datasets = ["boston"]

dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite"];

for model in models:
    for ds in datasets:
        for dialect in dialects:
            create_script(model , ds, dialect)

