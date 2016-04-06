from flask import Flask, render_template, request, url_for, redirect, flash
from flask import jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
# from pyelasticsearch import ElasticSearch
from datetime import timedelta
from make_db import (create_adoptable, create_breed, create_Breeds, create_Adoptables)
from models import db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage
import requests


app = Flask(__name__)
db = SQLAlchemy(app)
# es = ElasticSearch('http://23.253.111.129:9200/')


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

# API
# BREEDS
@app.route('/api/breeds/', methods = ['GET'])
def breeds_api():
	page = request.args.get('page')
	page_size = request.args.get('page_size')
	if page is None:
		page = 0
	else:
		page = int(page)
	if page_size is None:
		page_size = 5
	else:
		page_size = int(page_size)
	beginning = page*page_size
	end = (page*page_size) + page_size
	breeds = Breed.query.all()[beginning : end]
	breeds = update_breeds(convert_to_json(breeds))
	return jsonify(breeds=breeds)

@app.route('/api/breeds/<int:breed_id>', methods = ['GET'])
def breed_api(breed_id):
	breed = update_breed((Breed.query.get(breed_id)).to_json())
	return jsonify(breed=breed)




# ADOPTABLES
@app.route('/api/adoptables/', methods = ['GET'])
def adoptables_api():
	page = request.args.get('page')
	page_size = request.args.get('page_size')
	if page is None:
		page = 0
	else:
		page = int(page)
	if page_size is None:
		page_size = 5
	else:
		page_size = int(page_size)
	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = Adoptable.query.all()[beginning : end]
	adoptables = update_adoptables(convert_to_json(adoptables))
	return jsonify(adoptables=adoptables)

@app.route('/api/adoptables/<int:adoptable_id>', methods = ['GET'])
def adoptable_api(adoptable_id):
	adoptable = update_adoptable((Adoptable.query.get(adoptable_id)).to_json())
	return jsonify(adoptable=adoptable)

@app.route('/api/adoptables/breed/<int:breed_id>', methods = ['GET'])
def adoptablesByBreed_api(breed_id):
	page = request.args.get('page')
	page_size = request.args.get('page_size')
	if page is None:
		page = 0
	else:
		page = int(page)
	if page_size is None:
		page_size = 5
	else:
		page_size = int(page_size)

	adoptables = Adoptable.query.filter(AdoptableBreed.adoptable_id==Adoptable.id, AdoptableBreed.breed_id == breed_id)

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = adoptables[beginning : end]
	adoptables = update_adoptables(convert_to_json(adoptables))
	return jsonify(adoptables=adoptables)


@app.route('/api/adoptables/organization/<int:organization_id>', methods = ['GET'])
def adoptablesByOrganization_api(organization_id):
	page = request.args.get('page')
	page_size = request.args.get('page_size')
	if page is None:
		page = 0
	else:
		page = int(page)
	if page_size is None:
		page_size = 5
	else:
		page_size = int(page_size)

	adoptables = Adoptable.query.filter(Adoptable.org_id == organization_id)

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = adoptables[beginning : end]
	adoptables = update_adoptables(convert_to_json(adoptables))
	return jsonify(adoptables=adoptables)




# ORGANIZATIONS
@app.route('/api/organizations/', methods = ['GET'])
def organizations_api():
	page = request.args.get('page')
	page_size = request.args.get('page_size')
	if page is None:
		page = 0
	else:
		page = int(page)
	if page_size is None:
		page_size = 5
	else:
		page_size = int(page_size)
	beginning = page*page_size
	end = (page*page_size) + page_size
	organizations = Organization.query.all()[beginning : end]
	return jsonify(organizations=convert_to_json(organizations))

@app.route('/api/organizations/<int:organization_id>', methods = ['GET'])
def organization_api(organization_id):
	return jsonify(organization=(Organization.query.get(organization_id)).to_json())



# Helper functions
def convert_to_json(listToConvert):
	convertedList = []
	for item in listToConvert:
		convertedList.append(item.to_json())
	return convertedList


def update_breed(breed):
	image_info = BreedImage.query.filter(BreedImage.breed_id==breed['id'])
	images = []
	for i in image_info:
		images.append(i.url)
	breed['images'] = images

	return breed

def update_breeds(breeds):
	updatedBreeds = []
	for breed in breeds:
		updatedBreeds.append(update_breed(breed))
	return updatedBreeds



def update_adoptable(adoptable):
	breeds = []
	breed_ids = []
	breed_info = AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable['id'])
	for b in breed_info:
		breed_ids.append(b.breed_id)
		breeds.append(Breed.query.filter(Breed.id==b.breed_id).first().name)
	adoptable['breed_ids'] = breed_ids
	adoptable['breeds'] = breeds

	image_info = AdoptableImage.query.filter(AdoptableImage.adoptable_id==adoptable['id'])
	images = []
	for i in image_info:
		images.append(i.url)
	adoptable['images'] = images

	return adoptable

def update_adoptables(adoptables):
	updatedAdoptables = []
	for adoptable in adoptables:
		updatedAdoptables.append(update_adoptable(adoptable))
	return updatedAdoptables


if __name__ == '__main__':
	app.debug = True
	app.run()
