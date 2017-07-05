
from sklearn2sql_heroku.tests.classification import generic as class_gen

models = class_gen.get_models()
datasets = class_gen.get_datasets()

dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite"];

for model in models.keys():
    for ds in datasets.keys():
        print("TRAINING_MODEL" , model)
        for dialect in dialects:
            print("GENERATING_SQL_FOR" , model , ds, dialect)
            lSQL = class_gen.test_model(model , ds, dialect)
            print(lSQL)

