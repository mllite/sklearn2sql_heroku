import os, glob
from sklearn2sql_heroku.tests.regression import generic as reg_gen

models = reg_gen.get_models()
datasets = reg_gen.get_datasets()

dialects = ["db2", "hive", "mssql", "mysql", "oracle", "postgresql", "sqlite", "duckdb"];

print("PYTHON=timeout 180 python3\n\n")
ws_datasets_target = "";
for ds in datasets.keys():
        dirname = "tests/regression/" + ds
        dir_tgt = ""
        for filename in sorted(glob.glob(dirname + '/*.py')):
                bn = os.path.basename(filename);
                logfile = "logs/" +  bn.replace(".py" , ".log");
                # print("#PROCESSING FILE : " , filename, bn);
                print(bn + " : " , "\n\t", "-$(PYTHON)" , filename , " > " , logfile , " 2>&1");
                dir_tgt = dir_tgt + " " + bn

        print("\n" + ds + ": ", dir_tgt , "\n" , "\t\n");
        ws_datasets_target = ws_datasets_target + " " + ds;

print("\n\nws_datasets: ", ws_datasets_target , "\n" , "\t\n");


