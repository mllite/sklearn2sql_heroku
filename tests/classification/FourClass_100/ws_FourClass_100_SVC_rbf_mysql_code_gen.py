from sklearn2sql_heroku.tests.classification import generic as class_gen


class_gen.test_model("SVC_rbf" , "FourClass_100" , "mysql")
