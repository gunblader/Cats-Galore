from flask import Flask, render_template, request, url_for, redirect, flash
from flask import jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
# from pyelasticsearch import ElasticSearch
from datetime import timedelta
from make_db import (create_adoptable, create_breed, create_Breeds, create_Adoptables)
from models import db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage
import requests
import subprocess
import json
# import simplejson
import urllib
import os
os.environ['no_proxy'] = '127.0.0.1, localhost'


app = Flask(__name__)
db = SQLAlchemy(app)
# es = ElasticSearch('http://23.253.111.129:9200/')

# REAL THING

@app.route('/', methods=['GET','POST'])
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/breeds')
@app.route('/breeds/<breed>')
def breeds(breed=None):

    if breed is not None:
    	url = "http://catsgalore.me/api/breeds/" + breed
    	response = urllib.urlopen(url)
    	data1 = json.loads(response.read())
        return render_template('models/breed.html', breed=data['breed'] )
    else:
    	url = "http://catsgalore.me/api/breeds/" + "?page_size=100"
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
    return render_template('breeds.html', breeds=data['breeds'])

@app.route('/adoptables')
@app.route('/adoptables/<adoptable>')
def adoptables(adoptable=None):

    if adoptable is not None:
        url = "http://catsgalore.me/api/adoptables/" + adoptable
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
        return render_template('models/adoptable.html', adoptable=data['adoptable'] )
    else:
        url = "http://catsgalore.me/api/adoptables/" + + "?page_size=100"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
    return render_template('adoptables.html', adoptables=data['adoptables'])

@app.route('/organizations')
@app.route('/organizations/<organization>')
def organizations(organization=None):

    if organization is not None:
        url = "http://catsgalore.me/api/organizations/" + organization
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
        return render_template('models/organization.html', organization=data['organization'] )
    else:
    	url = "http://catsgalore.me/api/organizations/" + "?page_size=100"
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
    return render_template('organizations.html', organizations=data['organizations'])

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/runtests')
def tests(test=None):

    if test is not None:
        url = "http://catsgalore.me/api/runtests/"
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
    	return render_template('test.html', test=data['test'] )
    return render_template("test.html")

@app.route('/organizations/error')
def organizations_error():
	return render_template("errors/error_noOrganization.html")

@app.route('/breeds/error')
def breeds_error():
	return render_template("errors/error_noBreed.html")

@app.route('/adoptables/error')
def adoptables_error():
	return render_template("errors/error_noAdoptable.html")

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

# API

@app.route('/api/runtests', methods = ['GET'])
def run_tests():
    subprocess.call(['make', 'test'])
    f = open('tests.tmp', 'r')
    d = {}
    d['results'] = f.read().replace('\r\n', '<br />')
    f.close()
    return jsonify(d)

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
	breeds = Breed.query.limit(page_size).offset(beginning)
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
	adoptables = Adoptable.query.limit(page_size).offset(beginning)
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

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = Adoptable.query.filter(AdoptableBreed.adoptable_id==Adoptable.id, AdoptableBreed.breed_id == breed_id).limit(page_size).offset(beginning)
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

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = Adoptable.query.filter(Adoptable.org_id == organization_id).limit(page_size).offset(beginning)
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
	organizations = Organization.query.limit(page_size).offset(beginning)
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

# END OF REAL THING


# FAKE THING

# @app.route('/', methods=['GET','POST'])
# @app.route('/index')
# def index():
# 	return render_template("index.html")

# @app.route('/breeds')
# @app.route('/breeds/<breed>')
# def breeds(breed=None):

#     if breed is not None:
#         return render_template('models/breed.html', breed=breed_api(breed), adoptables=adoptablesByBreed_api(breed) )
#     else:
#     	breeds = breeds_api()
#     return render_template('breeds.html', breeds=breeds)

# @app.route('/adoptables')
# @app.route('/adoptables/<adoptable>')
# def adoptables(adoptable=None):

#     if adoptable is not None:
#         return render_template('models/adoptable.html', adoptable=adoptable_api(adoptable) )
#     else:
#         adoptables = adoptables_api()
#     return render_template('adoptables.html', adoptables=adoptables)

# @app.route('/organizations')
# @app.route('/organizations/<organization>')
# def organizations(organization=None):

#     if organization is not None:
#         return render_template('models/organization.html', organization=organization_api(organization), adoptables=adoptablesByOrganization_api(organization) )
#     else:
#     	organizations = organizations_api()
#     return render_template('organizations.html', organizations=organizations)

# @app.route('/about')
# def about():
# 	return render_template("about.html")

# @app.route('/organizations/error')
# def organizations_error():
# 	return render_template("errors/error_noOrganization.html")

# @app.route('/breeds/error')
# def breeds_error():
# 	return render_template("errors/error_noBreed.html")

# @app.route('/adoptables/error')
# def adoptables_error():
# 	return render_template("errors/error_noAdoptable.html")

# @app.route('/testAdoptables')
# def testAdoptable():
# 	results = create_Adoptables()
# 	return jsonify(results)

# @app.route('/testDB')
# def testDB():
# 	x = create_Breeds()
# 	y = create_Adoptables()
# 	results = {"Breeds Created": x, "Adoptables Creaded": y}
# 	return jsonify(results)


# # API
# # BREEDS
# @app.route('/api/breeds/', methods = ['GET'])
# def breeds_api():
# 	breeds = Breed.query.all()
# 	breeds = update_breeds(convert_to_json(breeds))
# 	return breeds

# @app.route('/api/breeds/<int:breed_id>', methods = ['GET'])
# def breed_api(breed_id):
# 	breed = update_breed((Breed.query.get(breed_id)).to_json())
# 	return breed



# # ADOPTABLES
# @app.route('/api/adoptables/', methods = ['GET'])
# def adoptables_api():
# 	adoptables = Adoptable.query.all()
# 	adoptables = update_adoptables(convert_to_json(adoptables))
# 	return adoptables

# @app.route('/api/adoptables/<int:adoptable_id>', methods = ['GET'])
# def adoptable_api(adoptable_id):
# 	adoptable = update_adoptable((Adoptable.query.get(adoptable_id)).to_json())
# 	return adoptable

# @app.route('/api/adoptables/breed/<int:breed_id>', methods = ['GET'])
# def adoptablesByBreed_api(breed_id):
# 	page = request.args.get('page')
# 	page_size = request.args.get('page_size')
# 	if page is None:
# 		page = 0
# 	else:
# 		page = int(page)
# 	if page_size is None:
# 		page_size = 4
# 	else:
# 		page_size = int(page_size)

# 	allAdoptables = Adoptable.query.all()
# 	adoptables = []
# 	for adoptable in allAdoptables:
# 		breeds = AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable.id)
# 		for breed in breeds:
# 			if breed.breed_id == breed_id:
# 				adoptables.append(adoptable)
# 				break
# 	beginning = page*page_size
# 	end = (page*page_size) + page_size

# 	adoptables = adoptables[beginning : end]
# 	adoptables = update_adoptables(convert_to_json(adoptables))
# 	return adoptables


# @app.route('/api/adoptables/organization/<int:organization_id>', methods = ['GET'])
# def adoptablesByOrganization_api(organization_id):
# 	page = request.args.get('page')
# 	page_size = request.args.get('page_size')
# 	if page is None:
# 		page = 0
# 	else:
# 		page = int(page)
# 	if page_size is None:
# 		page_size = 4
# 	else:
# 		page_size = int(page_size)

# 	allAdoptables = Adoptable.query.all()
# 	adoptables = []
# 	for adoptable in allAdoptables:
# 		if adoptable.org_id == organization_id:
# 			adoptables.append(adoptable)

# 	beginning = page*page_size
# 	end = (page*page_size) + page_size

# 	adoptables = adoptables[beginning : end]
# 	adoptables = update_adoptables(convert_to_json(adoptables))
# 	return adoptables



# # ORGANIZATIONS
# @app.route('/api/organizations/', methods = ['GET'])
# def organizations_api():
# 	organizations = Organization.query.all()
# 	organizations = convert_to_json(organizations)
# 	return organizations

# @app.route('/api/organizations/<int:organization_id>', methods = ['GET'])
# def organization_api(organization_id):
# 	organization = Organization.query.get(organization_id).to_json()
# 	return organization


# # Helper functions
# def convert_to_json(listToConvert):
# 	convertedList = []
# 	for item in listToConvert:
# 		convertedList.append(item.to_json())
# 	return convertedList


# def update_breed(breed):
# 	image_info = BreedImage.query.filter(BreedImage.breed_id==breed['id'])
# 	images = []
# 	for i in image_info:
# 		images.append(i.url)
# 	breed['images'] = images

# 	return breed

# def update_breeds(breeds):
# 	updatedBreeds = []
# 	for breed in breeds:
# 		updatedBreeds.append(update_breed(breed))
# 	return updatedBreeds



# def update_adoptable(adoptable):
# 	breeds = []
# 	breed_ids = []
# 	breed_info = AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable['id'])
# 	for b in breed_info:
# 		breed_ids.append(b.breed_id)
# 		breeds.append(Breed.query.filter(Breed.id==b.breed_id).first().name)
# 	adoptable['breed_ids'] = breed_ids
# 	adoptable['breeds'] = breeds

# 	image_info = AdoptableImage.query.filter(AdoptableImage.adoptable_id==adoptable['id'])
# 	images = []
# 	for i in image_info:
# 		images.append(i.url)
# 	adoptable['images'] = images

# 	return adoptable

# def update_adoptables(adoptables):
# 	updatedAdoptables = []
# 	for adoptable in adoptables:
# 		updatedAdoptables.append(update_adoptable(adoptable))
# 	return updatedAdoptables


# if __name__ == '__main__':
# 	app.debug = True
# 	app.run()

# END OF FAKE THING
