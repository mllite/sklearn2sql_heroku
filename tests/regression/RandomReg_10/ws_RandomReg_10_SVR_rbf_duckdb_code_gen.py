from sklearn2sql_heroku.tests.regression import generic as reg_gen


reg_gen.test_model("SVR_rbf" , "RandomReg_10" , "duckdb")
