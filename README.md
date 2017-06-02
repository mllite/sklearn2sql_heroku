# sklearn2sql_heroku

This is a Heroku web service client for experimenting with sklearn2sql.

Roughly speaking, the user provides a pickled scikit-learn model and gets a JSON containing the SQL code for deploying the model.

**Please note that this is a very experimental service. Use at your own risk** 

Early adopters feedback , improvement requests, hints and github issues are welcome.

The script `test_client.py` for a sample usage for this web service (running on `https://sklearn2sql.herokuapp.com/`). 

More sample scripts in the `tests` directory (WIP).
