from flask.ext.restless import APIManager
from models import app, db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage
from flask import json, jsonify, request




# BREEDS
@app.route('/breeds/', methods = ['GET'])
def breeds():
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

@app.route('/breeds/<int:breed_id>', methods = ['GET'])
def breed(breed_id):
	breed = update_breed((Breed.query.get(breed_id)).to_json())
	return jsonify(breed=breed)




# ADOPTABLES
@app.route('/adoptables/', methods = ['GET'])
def adoptables():
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

@app.route('/adoptables/<int:adoptable_id>', methods = ['GET'])
def adoptable(adoptable_id):
	adoptable = update_adoptable((Adoptable.query.get(adoptable_id)).to_json())
	return jsonify(adoptable=adoptable)

@app.route('/adoptables/breed/<int:breed_id>', methods = ['GET'])
def adoptablesByBreed(breed_id):
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

	allAdoptables = Adoptable.query.all()
	adoptables = []
	for adoptable in allAdoptables:
		if AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable.id).first().breed_id == breed_id:
			adoptables.append(adoptable)

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = adoptables[beginning : end]
	adoptables = update_adoptables(convert_to_json(adoptables))
	return jsonify(adoptables=adoptables)


@app.route('/adoptables/organization/<int:organization_id>', methods = ['GET'])
def adoptablesByOrganization(organization_id):
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

	allAdoptables = Adoptable.query.all()
	adoptables = []
	for adoptable in allAdoptables:
		if adoptable.org_id == organization_id:
			adoptables.append(adoptable)

	beginning = page*page_size
	end = (page*page_size) + page_size
	adoptables = adoptables[beginning : end]
	adoptables = update_adoptables(convert_to_json(adoptables))
	return jsonify(adoptables=adoptables)




# ORGANIZATIONS
@app.route('/organizations/', methods = ['GET'])
def organizations():
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

@app.route('/organizations/<int:organization_id>', methods = ['GET'])
def organization(organization_id):
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
	breed_info = AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable['id']).first()
	adoptable['breed_id'] = breed_info.breed_id
	adoptable['breed'] = Breed.query.filter(Breed.id==breed_info.breed_id).first().name

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


if __name__ == "__main__":
	app.run(debug=True)