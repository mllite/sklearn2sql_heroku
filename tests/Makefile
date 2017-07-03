PYTHON=python3


classification/test_client_iris_large_models.py  :  
	 -$(PYTHON)  tests/classification/test_client_iris_large_models.py  >  logs/classification_test_client_iris_large_models.log  2>&1
classification/test_client_iris_many_models.py  :  
	 -$(PYTHON)  tests/classification/test_client_iris_many_models.py  >  logs/classification_test_client_iris_many_models.log  2>&1


 classification :  classification/test_client_iris_many_models.py classification/test_client_iris_large_models.py  
 

databases/test_client_bad_model.py  :  
	 -$(PYTHON)  tests/databases/test_client_bad_model.py  >  logs/databases_test_client_bad_model.log  2>&1
databases/test_client_db2.py  :  
	 -$(PYTHON)  tests/databases/test_client_db2.py  >  logs/databases_test_client_db2.log  2>&1
databases/test_client_hive.py  :  
	 -$(PYTHON)  tests/databases/test_client_hive.py  >  logs/databases_test_client_hive.log  2>&1
databases/test_client_mssql.py  :  
	 -$(PYTHON)  tests/databases/test_client_mssql.py  >  logs/databases_test_client_mssql.log  2>&1
databases/test_client_mysql.py  :  
	 -$(PYTHON)  tests/databases/test_client_mysql.py  >  logs/databases_test_client_mysql.log  2>&1
databases/test_client_non_supported_dialect.py  :  
	 -$(PYTHON)  tests/databases/test_client_non_supported_dialect.py  >  logs/databases_test_client_non_supported_dialect.log  2>&1
databases/test_client_oracle.py  :  
	 -$(PYTHON)  tests/databases/test_client_oracle.py  >  logs/databases_test_client_oracle.log  2>&1
databases/test_client_pgsql.py  :  
	 -$(PYTHON)  tests/databases/test_client_pgsql.py  >  logs/databases_test_client_pgsql.log  2>&1
databases/test_client_sqlite.py  :  
	 -$(PYTHON)  tests/databases/test_client_sqlite.py  >  logs/databases_test_client_sqlite.log  2>&1


 databases :  databases/test_client_sqlite.py databases/test_client_pgsql.py databases/test_client_oracle.py databases/test_client_non_supported_dialect.py databases/test_client_mysql.py databases/test_client_mssql.py databases/test_client_hive.py databases/test_client_db2.py databases/test_client_bad_model.py  
 

regression/test_client_boston_many_models.py  :  
	 -$(PYTHON)  tests/regression/test_client_boston_many_models.py  >  logs/regression_test_client_boston_many_models.log  2>&1


 regression :  regression/test_client_boston_many_models.py  
 


# ********************************************** 

all:  databases classification regression 
	

build-test :  classification regression 
	

