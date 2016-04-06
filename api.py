from flask.ext.restless import APIManager
from models import app, db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage
from flask import json, jsonify, request




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

	allAdoptables = Adoptable.query.all()
	adoptables = []
	for adoptable in allAdoptables:
		breeds = AdoptableBreed.query.filter(AdoptableBreed.adoptable_id==adoptable.id)
		for breed in breeds:
			if breed.breed_id == breed_id:
				adoptables.append(adoptable)
				break

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


if __name__ == "__main__":
	app.run(debug=True)