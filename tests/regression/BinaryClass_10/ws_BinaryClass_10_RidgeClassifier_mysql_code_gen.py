from sklearn2sql_heroku.tests.classification import generic as class_gen


class_gen.test_model("RidgeClassifier" , "BinaryClass_10" , "mysql")
