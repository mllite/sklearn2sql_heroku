library(caret, quiet = TRUE)
library(base64enc)
library(httr, quiet = TRUE)
library(mlbench)

data(BostonHousing)
BostonHousing$chas = as.numeric(BostonHousing$chas)


test_ws_sql_gen = function(model , dialect) {
    WS_URL = "https://sklearn2sql.herokuapp.com/model"
    WS_URL = "http://localhost:1888/model"
    model_serialized <- serialize(model, NULL)
    b64_data = base64encode(model_serialized)
    data = list(Name = "xgboost_test_model", SerializedModel = b64_data , SQLDialect = dialect , Mode="caret")
    r = POST(WS_URL, body = data, encode = "json")
    # print(r)
    content = content(r)
    # print(content)
    lSQL = content$model$SQLGenrationResult[[1]]$SQL # content["model"]["SQLGenrationResult"][0]["SQL"]
    return(lSQL);
}



create_dataset = function(ds_name) {
    dataset = BostonHousing
    return(dataset)
}


create_model  =  function(model_name , ds_name) {
    dataset = create_dataset(ds_name)
    model <- train(medv ~ ., data = dataset, method = model_name)    

    return(model)
}


test_caret_model = function(model_name , ds_name, dialect) {
     set.seed(1960)
     model = create_model(model_name , ds_name)
     lModelSQL = test_ws_sql_gen(model, dialect)
     cat(lModelSQL)
}
