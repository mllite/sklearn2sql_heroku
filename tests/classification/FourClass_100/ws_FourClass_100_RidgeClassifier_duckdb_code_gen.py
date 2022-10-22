from sklearn2sql_heroku.tests.classification import generic as class_gen


class_gen.test_model("RidgeClassifier" , "FourClass_100" , "duckdb")
