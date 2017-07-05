from sklearn2sql_heroku.tests.classification import generic as class_gen


class_gen.test_model("SGDClassifier" , "BinaryClass_100" , "postgresql")
