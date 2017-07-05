from sklearn2sql_heroku.tests.regression import generic as reg_gen


reg_gen.test_model("GradientBoostingRegressor" , "freidman3" , "mysql")
