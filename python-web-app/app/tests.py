from io             import StringIO
from unittest       import main, TestCase
from models 		import Adoptable, Breed, Organization
import api_calls
import requests
import json

#class MainTestCase(unittest.TestCase):
class MainTestCase(TestCase):

	# ----
    # API Calls
    # ----

    # ----
    # Adoptables API Calls
    # ----

	def test_adoptables_list_api_1(self):
	    api_base = "http://api.petfinder.com/pet.find" + api_calls.PETFINDER_KEY
	    api_tail = "&animal=cat&location=78705&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_adoptables_list_api_2(self):
	    api_base = "http://api.petfinder.com/pet.find" + api_calls.PETFINDER_KEY
	    api_tail = "&animal=cat&location=78705&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertNotRegexpMatches(r.text, "(unauthorized key)")

	def test_adoptables_list_api_3(self):
	    api_base = "http://api.petfinder.com/pet.find" + "?key=fakekey"
	    api_tail = "&animal=cat&location=78705&count=10&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")

	def test_get_single_adoptable_api_1(self):
	    api_base = "http://api.petfinder.com/pet.get" + api_calls.PETFINDER_KEY
	    api_tail = "&id=" + str(1) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_adoptable_api_2(self):
	    api_base = "http://api.petfinder.com/pet.get" + "?key=fakekey"
	    api_tail = "&id=" + str(1) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")

	def test_get_single_adoptable_api_3(self):
	    api_base = "http://api.petfinder.com/pet.get" + "?key=fakekey"
	    api_tail = "&id=" + str(1) + "&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")

    # ----
    # Breeds API Calls
    # ----

	def test_get_breeds_list_api_1(self):
	    api_base = "http://api.petfinder.com/breeds.list" + api_calls.PETFINDER_KEY
	    api_tail = "&animal=cat&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_breeds_list_api_2(self):
	    api_base = "http://api.petfinder.com/breeds.list" + api_calls.PETFINDER_KEY
	    api_tail = "&animal=cat&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertNotRegexpMatches(r.text, "(unauthorized key)")

	def test_get_breeds_list_api_3(self):
	    api_base = "http://api.petfinder.com/breeds.list" + "?key=fakekey"
	    api_tail = "&animal=cat&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")

	def test_get_single_breed_api_1(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + api_calls.WOLFRAMALPHA_APPID
	    api_tail = "&input=" + "Abyssinian" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_single_breed_api_2(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + api_calls.WOLFRAMALPHA_APPID
	    api_tail = "&input=" + "Abyssinian" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertNotRegexpMatches(r.text, "(Invalid appid)")

	def test_get_single_breed_api_3(self):
	    api_base = "http://api.wolframalpha.com/v2/query" + "?appid=fakeappid"
	    api_tail = "&input=" + "Abyssinian" + "(cat%20breed)&format=plaintext"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(Invalid appid)")

    # ----
    # Organizations API Calls
    # ----

	def test_get_organizations_list_api_1(self):
	    api_base = "http://api.petfinder.com/shelter.find" + api_calls.PETFINDER_KEY
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertEqual(r.status_code, 200)

	def test_get_organizations_list_api_2(self):
	    api_base = "http://api.petfinder.com/shelter.find" + "?key=fakekey"
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")

	def test_get_organizations_list_api_3(self):
	    api_base = "http://api.petfinder.com/shelter.find" + "?key=fakekey"
	    api_tail = "&location=78705&format=json"
	    r = requests.get(api_base + api_tail)
	    self.assertRegexpMatches(r.text, "(unauthorized key)")


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
    # Breed Model
    # ----

	def test_model_breed_1 (self) :
		temp = Breed(name='a', types='b', personality='c', hairLength=1, weight=2, size='d', description='f', origin = 'g', shedding = 'i', grooming = 'j', recognitions = 'k', wikiLink = 'l')
		self.assertEqual(temp.name, 'a')
		self.assertEqual(temp.types, 'b')
		self.assertEqual(temp.personality, 'c')
		self.assertEqual(temp.hairLength, 1)
		self.assertEqual(temp.weight, 2)
		self.assertEqual(temp.size, 'd')
		self.assertEqual(temp.description, 'f')
		self.assertEqual(temp.origin, 'g')
		self.assertEqual(temp.shedding, 'i')
		self.assertEqual(temp.grooming, 'j')
		self.assertEqual(temp.recognitions, 'k')
		self.assertEqual(temp.wikiLink, 'l')

	def test_model_breed_2 (self) :
		temp = Breed(name='', types='', personality='', hairLength=0, weight=0, size='', description='', origin = '', shedding = '', grooming = '', recognitions = '', wikiLink = '')
		self.assertEqual(temp.name, '')
		self.assertEqual(temp.types, '')
		self.assertEqual(temp.personality, '')
		self.assertEqual(temp.hairLength, 0)
		self.assertEqual(temp.weight, 0)
		self.assertEqual(temp.description, '')
		self.assertEqual(temp.origin, '')
		self.assertEqual(temp.shedding, '')
		self.assertEqual(temp.grooming, '')
		self.assertEqual(temp.recognitions, '')
		self.assertEqual(temp.wikiLink, '')

	def test_model_breed_3 (self) :
		temp = Breed(name='the', types='cat', personality='in', hairLength=111, weight=222, size='small', description='the', origin = 'hat', shedding = 'not', grooming = 'very', recognitions = 'smart', wikiLink = 'today')
		self.assertEqual(temp.name, 'the')
		self.assertEqual(temp.types, 'cat')
		self.assertEqual(temp.personality, 'in')
		self.assertEqual(temp.hairLength, 111)
		self.assertEqual(temp.weight, 222)
		self.assertEqual(temp.size, 'small')
		self.assertEqual(temp.description, 'the')
		self.assertEqual(temp.origin, 'hat')
		self.assertEqual(temp.shedding, 'not')
		self.assertEqual(temp.grooming, 'very')
		self.assertEqual(temp.recognitions, 'smart')
		self.assertEqual(temp.wikiLink, 'today')

    # ----
    # Organization Model
    # ----

	def test_model_organization_1 (self) :
		temp = Organization(name='a', address1='b', address2='c', city='d', state='e', description='f', postalCode = 1, country = 'g', phone = 2, fax = 3, email = 'h', url = 'i', latitude = 4.0, longitude = 5.0)
		self.assertEqual(temp.name, 'a')
		self.assertEqual(temp.address1, 'b')
		self.assertEqual(temp.address2, 'c')
		self.assertEqual(temp.city, 'd')
		self.assertEqual(temp.state, 'e')
		self.assertEqual(temp.description, 'f')
		self.assertEqual(temp.postalCode, 1)
		self.assertEqual(temp.country, 'g')
		self.assertEqual(temp.phone, 2)
		self.assertEqual(temp.fax, 3)
		self.assertEqual(temp.email, 'h')
		self.assertEqual(temp.url, 'i')
		self.assertEqual(temp.latitude, 4.0)
		self.assertEqual(temp.longitude, 5.0)

	def test_model_organization_2 (self) :
		temp = Organization(name='', address1='', address2='', city='', state='', description='', postalCode = 0, country = '', phone = 0, fax = 0, email = '', url = '', latitude = 0.0, longitude = 0.0)
		self.assertEqual(temp.name, '')
		self.assertEqual(temp.address1, '')
		self.assertEqual(temp.address2, '')
		self.assertEqual(temp.city, '')
		self.assertEqual(temp.state, '')
		self.assertEqual(temp.description, '')
		self.assertEqual(temp.postalCode, 0)
		self.assertEqual(temp.country, '')
		self.assertEqual(temp.phone, 0)
		self.assertEqual(temp.fax, 0)
		self.assertEqual(temp.email, '')
		self.assertEqual(temp.latitude, 0.0)
		self.assertEqual(temp.longitude, 0.0)

	def test_model_organization_3 (self) :
		temp = Organization(name='the', address1='cat', address2='in', city='the', state='hat', description='is', postalCode = 1, country = 'not', phone = 2, fax = 3, email = 'nice', url= 'huh', latitude = 4.0, longitude = 5.0)
		self.assertEqual(temp.name, 'the')
		self.assertEqual(temp.address1, 'cat')
		self.assertEqual(temp.address2, 'in')
		self.assertEqual(temp.city, 'the')
		self.assertEqual(temp.state, 'hat')
		self.assertEqual(temp.description, 'is')
		self.assertEqual(temp.postalCode, 1)
		self.assertEqual(temp.country, 'not')
		self.assertEqual(temp.phone, 2)
		self.assertEqual(temp.fax, 3)
		self.assertEqual(temp.email, 'nice')
		self.assertEqual(temp.url, 'huh')
		self.assertEqual(temp.latitude, 4.0)
		self.assertEqual(temp.longitude, 5.0)

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
