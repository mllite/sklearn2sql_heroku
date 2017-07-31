from sklearn2sql_heroku.tests.regression import generic as reg_gen


reg_gen.test_model("LGBMRegressor" , "freidman3" , "postgresql")
