from flask import Flask, render_template, request, url_for, redirect, flash
from flask import jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from pyelasticsearch import ElasticSearch
from datetime import timedelta
from make_db import (create_adoptable, create_breed, create_Breeds, create_Adoptables)
import requests


app = Flask(__name__)
db = SQLAlchemy(app)
es = ElasticSearch('http://23.253.111.129:9200/')


@app.route('/', methods=['GET','POST'])
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/breeds')
def breeds():
	return render_template("breeds.html")

@app.route('/testAdoptables')
def testAdoptable():
	results = create_Adoptables()
	return jsonify(results)

@app.route('/testDB')
def testDB():
	x = create_Breeds()
	y = create_Adoptables()
	results = {"Breeds Created": x, "Adoptables Creaded": y}
	return jsonify(results)

@app.route('/adoptables')
def adoptables():
	return render_template("adoptables.html")

@app.route('/organizations')
def organizations():
	return render_template("organizations.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/breeds/1')
def breeds_1():
	return render_template("models/breeds/1.html")

@app.route('/breeds/2')
def breeds_2():
	return render_template("models/breeds/2.html")

@app.route('/breeds/3')
def breeds_3():
	return render_template("models/breeds/3.html")

@app.route('/adoptables/1')
def adoptables_1():
	return render_template("models/adoptables/1.html")

@app.route('/adoptables/2')
def adoptables_2():
	return render_template("models/adoptables/2.html")

@app.route('/adoptables/3')
def adoptables_3():
	return render_template("models/adoptables/3.html")

@app.route('/organizations/1')
def organizations_1():
	return render_template("models/organizations/1.html")

@app.route('/organizations/2')
def organizations_2():
	return render_template("models/organizations/2.html")

@app.route('/organizations/3')
def organizations_3():
	return render_template("models/organizations/3.html")

@app.route('/organizations/error')
def organizations_error():
	return render_template("errors/error_noOrganization.html")

@app.route('/breeds/error')
def breeds_error():
	return render_template("errors/error_noBreed.html")

@app.route('/adoptables/error')
def adoptables_error():
	return render_template("errors/error_noAdoptable.html")

if __name__ == '__main__':
	app.debug = True
	app.run()
