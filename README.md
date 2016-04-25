Check out Wiki for more info
https://github.com/gunblader/cs373-idb/wiki

# Getting Flask up and running
### Install virtualenv
```
pip install virtualenv
virtualenv .virtualenv -p python2.7
cd .virtualenv
```
### Install flask + dependencies
```
pip install flask
pip install flask-sqlalchemy
pip install mysql-python
pip install requests
pip pyelasticsearch
```
### Start virtualenv and run app
```
cd .virtualenv
source bin/activate
cd cs373-idb
cd pythonwebapp/app/
python app.py
```
