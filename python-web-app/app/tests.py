from io             import StringIO
from unittest       import main, TestCase
from models 		import *
from api_calls		import *
from app 			import *
import requests
import json

#class MainTestCase(unittest.TestCase):
class MainTestCase(TestCase):

    # ----
    # Adoptables External API Calls
    # ----

	def test_adoptables_list_api_1(self):
	    api_base = "http://api.petfinder.com/pet.find" + PETFINDER_KEY
	    api_tail = "&animal=cat&location=78705&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_adoptables_list_api_2(self):
	    api_base = "http://api.petfinder.com/pet.find" + PETFINDER_KEY
	    api_tail = "&animal=potato&location=00000&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_adoptables_list_api_3(self):
	    api_base = "http://api.petfinder.com/pet.find" + "?key=fakekey"
	    api_tail = "&animal=cat&location=78705&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegex(r.text, "(unauthorized key)")

	def test_adoptables_list_api_4(self):
		try:
			get_adoptables_list()
		except:
			assert (False)

	def test_get_single_adoptable_api_1(self):
	    api_base = "http://api.petfinder.com/pet.get" + PETFINDER_KEY
	    api_tail = "&id=" + str(1) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_adoptable_api_2(self):
	    api_base = "http://api.petfinder.com/pet.get" + PETFINDER_KEY
	    api_tail = "&id=" + str(99) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_adoptable_api_3(self):
	    api_base = "http://api.petfinder.com/pet.get" + "?key=fakekey"
	    api_tail = "&id=" + str(1) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegex(r.text, "(unauthorized key)")

	def test_get_single_adoptable_api_4(self):
		try:
			get_single_adoptable(1)
		except:
			assert (False)

    # ----
    # Breeds External API Calls
    # ----

	# def test_get_breeds_list_api_1(self):
	#     api_base = "http://api.petfinder.com/breeds.list" + PETFINDER_KEY
	#     api_tail = "&animal=cat&format=json"
	#     r = requests.get(api_base + api_tail)
	#     self.assertEqual(r.status_code, 200)

	# def test_get_breeds_list_api_2(self):
	#     api_base = "http://api.petfinder.com/breeds.list" + PETFINDER_KEY
	#     api_tail = "&animal=potato&format=json"
	#     r = requests.get(api_base + api_tail)
	#     self.assertEqual(r.status_code, 200)

	# def test_get_breeds_list_api_3(self):
	#     api_base = "http://api.petfinder.com/breeds.list" + "?key=fakekey"
	#     api_tail = "&animal=cat&format=json"
	#     r = requests.get(api_base + api_tail)
	#     self.assertRegexpMatches(r.text, "(unauthorized key)")

	def test_get_single_breed_api_1(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + WOLFRAMALPHA_APPID
	    api_tail = "&input=" + "Abyssinian" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_breed_api_2(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + WOLFRAMALPHA_APPID
	    api_tail = "&input=" + "potato" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_breed_api_3(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + "?appid=fakeappid"
	    api_tail = "&input=" + "Abyssinian" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertRegex(r.text, "(Invalid appid)")

	def test_get_single_breed_api_4(self):
	    try:
	    	get_single_breed("Abyssinian")
	    except:
	    	assert (False)

    # ----
    # Organizations External API Calls
    # ----

	def test_get_organizations_list_api_1(self):
	    api_base = "http://api.petfinder.com/shelter.find" + PETFINDER_KEY
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_organizations_list_api_2(self):
	    api_base = "http://api.petfinder.com/shelter.find" + "?key=fakekey"
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegex(r.text, "(unauthorized key)")

	def test_get_organizations_list_api_3(self):
	    api_base = "http://api.petfinder.com/shelter.find" + "?key=fakekey"
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegex(r.text, "(unauthorized key)")

	def test_get_organizations_list_api_4(self):
	    try:
	    	get_organizations_list()
	    except:
	    	assert (False)

	# ----
    # Adoptable Model
    # ----

	def test_model_adoptable_1 (self) :
		temp = Adoptable(name='a', mixed='c', age=1, sex='e', size='f', org_id=2)
		self.assertEqual(temp.name, 'a')
		self.assertEqual(temp.mixed, 'c')
		self.assertEqual(temp.age, 1)
		self.assertEqual(temp.sex, 'e')
		self.assertEqual(temp.size, 'f')
		self.assertEqual(temp.org_id, 2)

	def test_model_adoptable_2 (self) :
		temp = Adoptable(name='', mixed='', age=0, sex='', size='', org_id=0)
		self.assertEqual(temp.name, '')
		self.assertEqual(temp.mixed, '')
		self.assertEqual(temp.age, 0)
		self.assertEqual(temp.sex, '')
		self.assertEqual(temp.size, '')
		self.assertEqual(temp.org_id, 0)

	def test_model_adoptable_3 (self) :
		temp = Adoptable(name='the', mixed='in', age=111, sex='the', size='hat', org_id=222)
		self.assertEqual(temp.name, 'the')
		self.assertEqual(temp.mixed, 'in')
		self.assertEqual(temp.age, 111)
		self.assertEqual(temp.sex, 'the')
		self.assertEqual(temp.size, 'hat')
		self.assertEqual(temp.org_id, 222)


	# ----
	# Adoptable Breed
	# -----

	def test_model_adoptable_breed_1 (self) :
		temp = AdoptableBreed(adoptable_id=1, breed_id=1)
		self.assertEqual(temp.adoptable_id, 1)
		self.assertEqual(temp.breed_id, 1)

	def test_model_adoptable_breed_2 (self) :
		temp = AdoptableBreed(adoptable_id=0, breed_id=0)
		self.assertEqual(temp.adoptable_id, 0)
		self.assertEqual(temp.breed_id, 0)

	def test_model_adoptable_breed_3 (self) :
		temp = AdoptableBreed(adoptable_id=111, breed_id=222)
		self.assertEqual(temp.adoptable_id, 111)
		self.assertEqual(temp.breed_id, 222)

    # ----
    # Breed Model
    # ----

	def test_model_breed_1 (self) :
		temp = Breed(name='a', types='b', personality='c', hairlength=1, weight=2, size='d', description='f', origin = 'g', shedding = 'i', grooming = 'j', recognitions = 'k', wikilink = 'l')
		self.assertEqual(temp.name, 'a')
		self.assertEqual(temp.types, 'b')
		self.assertEqual(temp.personality, 'c')
		self.assertEqual(temp.hairlength, 1)
		self.assertEqual(temp.weight, 2)
		self.assertEqual(temp.size, 'd')
		self.assertEqual(temp.description, 'f')
		self.assertEqual(temp.origin, 'g')
		self.assertEqual(temp.shedding, 'i')
		self.assertEqual(temp.grooming, 'j')
		self.assertEqual(temp.recognitions, 'k')
		self.assertEqual(temp.wikilink, 'l')

	def test_model_breed_2 (self) :
		temp = Breed(name='', types='', personality='', hairlength=0, weight=0, size='', description='', origin = '', shedding = '', grooming = '', recognitions = '', wikilink = '')
		self.assertEqual(temp.name, '')
		self.assertEqual(temp.types, '')
		self.assertEqual(temp.personality, '')
		self.assertEqual(temp.hairlength, 0)
		self.assertEqual(temp.weight, 0)
		self.assertEqual(temp.description, '')
		self.assertEqual(temp.origin, '')
		self.assertEqual(temp.shedding, '')
		self.assertEqual(temp.grooming, '')
		self.assertEqual(temp.recognitions, '')
		self.assertEqual(temp.wikilink, '')

	def test_model_breed_3 (self) :
		temp = Breed(name='the', types='cat', personality='in', hairlength=111, weight=222, size='small', description='the', origin = 'hat', shedding = 'not', grooming = 'very', recognitions = 'smart', wikilink = 'today')
		self.assertEqual(temp.name, 'the')
		self.assertEqual(temp.types, 'cat')
		self.assertEqual(temp.personality, 'in')
		self.assertEqual(temp.hairlength, 111)
		self.assertEqual(temp.weight, 222)
		self.assertEqual(temp.size, 'small')
		self.assertEqual(temp.description, 'the')
		self.assertEqual(temp.origin, 'hat')
		self.assertEqual(temp.shedding, 'not')
		self.assertEqual(temp.grooming, 'very')
		self.assertEqual(temp.recognitions, 'smart')
		self.assertEqual(temp.wikilink, 'today')

	# ----
    # Breed Organization Model
    # ----

	def test_model_breed_organization_1 (self) :
		temp = BreedOrganization(breed_id=1, organization_id=1)
		self.assertEqual(temp.breed_id, 1)
		self.assertEqual(temp.organization_id, 1)

	def test_model_breed_organization_2 (self) :
		temp = BreedOrganization(breed_id=0, organization_id=0)
		self.assertEqual(temp.breed_id, 0)
		self.assertEqual(temp.organization_id, 0)

	def test_model_breed_organization_3 (self) :
		temp = BreedOrganization(breed_id=111, organization_id=222)
		self.assertEqual(temp.breed_id, 111)
		self.assertEqual(temp.organization_id, 222)


    # ----
    # Organization Model
    # ----

	def test_model_organization_1 (self) :
		temp = Organization(name='a', address1='b', address2='c', city='d', state='e', description='f', postalcode = 1, country = 'g', phone = 2, fax = 3, email = 'h', url = 'i', latitude = 4.0, longitude = 5.0)
		self.assertEqual(temp.name, 'a')
		self.assertEqual(temp.address1, 'b')
		self.assertEqual(temp.address2, 'c')
		self.assertEqual(temp.city, 'd')
		self.assertEqual(temp.state, 'e')
		self.assertEqual(temp.description, 'f')
		self.assertEqual(temp.postalcode, 1)
		self.assertEqual(temp.country, 'g')
		self.assertEqual(temp.phone, 2)
		self.assertEqual(temp.fax, 3)
		self.assertEqual(temp.email, 'h')
		self.assertEqual(temp.url, 'i')
		self.assertEqual(temp.latitude, 4.0)
		self.assertEqual(temp.longitude, 5.0)

	def test_model_organization_2 (self) :
		temp = Organization(name='', address1='', address2='', city='', state='', description='', postalcode = 0, country = '', phone = 0, fax = 0, email = '', url = '', latitude = 0.0, longitude = 0.0)
		self.assertEqual(temp.name, '')
		self.assertEqual(temp.address1, '')
		self.assertEqual(temp.address2, '')
		self.assertEqual(temp.city, '')
		self.assertEqual(temp.state, '')
		self.assertEqual(temp.description, '')
		self.assertEqual(temp.postalcode, 0)
		self.assertEqual(temp.country, '')
		self.assertEqual(temp.phone, 0)
		self.assertEqual(temp.fax, 0)
		self.assertEqual(temp.email, '')
		self.assertEqual(temp.latitude, 0.0)
		self.assertEqual(temp.longitude, 0.0)

	def test_model_organization_3 (self) :
		temp = Organization(name='the', address1='cat', address2='in', city='the', state='hat', description='is', postalcode = 1, country = 'not', phone = 2, fax = 3, email = 'nice', url= 'huh', latitude = 4.0, longitude = 5.0)
		self.assertEqual(temp.name, 'the')
		self.assertEqual(temp.address1, 'cat')
		self.assertEqual(temp.address2, 'in')
		self.assertEqual(temp.city, 'the')
		self.assertEqual(temp.state, 'hat')
		self.assertEqual(temp.description, 'is')
		self.assertEqual(temp.postalcode, 1)
		self.assertEqual(temp.country, 'not')
		self.assertEqual(temp.phone, 2)
		self.assertEqual(temp.fax, 3)
		self.assertEqual(temp.email, 'nice')
		self.assertEqual(temp.url, 'huh')
		self.assertEqual(temp.latitude, 4.0)
		self.assertEqual(temp.longitude, 5.0)

	# ----
    # Adoptable Image Model
    # ----

	def test_model_adoptable_image_1 (self) :
		temp = AdoptableImage(url='a', adoptable_id=1)
		self.assertEqual(temp.url, 'a')
		self.assertEqual(temp.adoptable_id, 1)

	def test_model_adoptable_image_2 (self) :
		temp = AdoptableImage(url='', adoptable_id=0)
		self.assertEqual(temp.url, '')
		self.assertEqual(temp.adoptable_id, 0)

	def test_model_adoptable_image_3 (self) :
		temp = AdoptableImage(url='http://example.com', adoptable_id=111)
		self.assertEqual(temp.url, 'http://example.com')
		self.assertEqual(temp.adoptable_id, 111)

    # ----
    # Breed Image Model
    # ----

	def test_model_breed_image_1 (self) :
		temp = BreedImage(url='a', breed_id=1)
		self.assertEqual(temp.url, 'a')
		self.assertEqual(temp.breed_id, 1)

	def test_model_breed_image_2 (self) :
		temp = BreedImage(url='', breed_id=0)
		self.assertEqual(temp.url, '')
		self.assertEqual(temp.breed_id, 0)

	def test_model_breed_image_3 (self) :
		temp = BreedImage(url='http://example.com', breed_id=111)
		self.assertEqual(temp.url, 'http://example.com')
		self.assertEqual(temp.breed_id, 111)


	# ----
	# Breeds Internal API Calls
	# ----

	def test_breeds_api_1(self):
		with app.test_request_context():
			try:
				breeds_api()
			except:
				assert (False)

	def test_breeds_api_2(self):
		with app.test_request_context():
			response = breeds_api()
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_breeds_api_3(self):
		with app.test_request_context():
			try:
				response = breeds_api().get_data()
				data = json.loads(response)
				data['breeds'][1]['origin']
			except:
				assert (False)

	def test_breed_api_1(self):
		with app.test_request_context():
			try:
				breed_api(1)
			except:
				assert (False)

	def test_breed_api_2(self):
		with app.test_request_context():
			response = breed_api(1)
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_breed_api_3(self):
		with app.test_request_context():
			try:
				response = breed_api(1).get_data()
				data = json.loads(response)
				data['breed']['origin']
			except:
				assert (False)


	# ----
	# Adoptables Internal API Calls
	# ----

	def test_adoptables_api_1(self):
		with app.test_request_context():
			try:
				adoptables_api()
			except:
				assert (False)

	def test_adoptables_api_2(self):
		with app.test_request_context():
			response = adoptables_api()
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_adoptables_api_3(self):
		with app.test_request_context():
			try:
				response = adoptables_api().get_data()
				data = json.loads(response)
				data['adoptables'][1]['age']
			except:
				assert (False)

	def test_adoptable_api_1(self):
		with app.test_request_context():
			try:
				adoptable_api(1)
			except:
				assert (False)

	def test_adoptable_api_2(self):
		with app.test_request_context():
			response = adoptable_api(1)
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_adoptable_api_3(self):
		with app.test_request_context():
			try:
				response = adoptable_api(1).get_data()
				data = json.loads(response)
				data['adoptable']['age']
			except:
				assert (False)

	def test_adoptablesByBreed_api_1(self):
		with app.test_request_context():
			try:
				adoptablesByBreed_api(1)
			except:
				assert (False)

	def test_adoptablesByBreed_api_2(self):
		with app.test_request_context():
			response = adoptablesByBreed_api(1)
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_adoptablesByBreed_api_3(self):
		with app.test_request_context():
			try:
				response = adoptablesByBreed_api('Abyssinian').get_data()
				data = json.loads(response)
				data['adoptables']
			except:
				assert (False)

	def test_adoptablesByOrganization_api_1(self):
		with app.test_request_context():
			try:
				adoptablesByOrganization_api(1)
			except:
				assert (False)

	def test_adoptablesByOrganization_api_2(self):
		with app.test_request_context():
			response = adoptablesByOrganization_api(1)
			expectedResponse = {""}
			self.assertNotEqual(response, expectedResponse)

	def test_adoptablesByOrganization_api_3(self):
		with app.test_request_context():
			try:
				response = adoptablesByOrganization_api(1).get_data()
				data = json.loads(response)
				data['adoptables']
			except:
				assert (False)


	# # ----
	# # Organizations Internal API Calls
	# # ----

	def test_organizations_api_1(self):
		with app.test_request_context():
			try:
				organizations_api()
			except:
				assert (False)

	def test_organizations_api_2(self):
		with app.test_request_context():
			json = organizations_api()
			expectedJson = {""}
			self.assertNotEqual(json, expectedJson)

	def test_organization_api_1(self):
		with app.test_request_context():
			try:
				organization_api(1)
			except:
				assert (False)

	def test_organization_api_2(self):
		with app.test_request_context():
			json = organization_api(1)
			expectedJson = {""}
			self.assertNotEqual(json, expectedJson)


	# ---------
	# Default
	# ---------	

	def test_two_and_two(self):
		four = 2 + 2
		self.assertEqual(four, 4)
		self.assertNotEqual(four, 5)
		self.assertNotEqual(four, 6)
		self.assertNotEqual(four, 22)

if __name__ == '__main__':
    #unittest.main()
    main()
