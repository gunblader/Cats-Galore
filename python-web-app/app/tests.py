from io             import StringIO
from urllib.request import urlopen
from unittest       import main, TestCase
from models 		import Adoptable, Breed, Organization
import json, postgresql

class MainTestCase(unittest.TestCase):
	# ----
    # read
    # ----

    def test_adoptable_1 (self) :
        temp = Adoptable(name='a', breed='b', mixed='c', age=1, sex='e', size='f', org_id=2, images_id=3)
        self.assertEqual(temp.name, 'a')
        self.assertEqual(temp.breed, 'b')
        self.assertEqual(temp.mixed, 'c')
        self.assertEqual(temp.age, 1)
        self.assertEqual(temp.sex, 'e')
        self.assertEqual(temp.size, 'f')
        self.assertEqual(temp.org_id, 2)
        self.assertEqual(temp.images_id, 3)

    def test_adoptable_2 (self) :
        temp = Adoptable()
        self.assertEqual(temp.name, None)
        self.assertEqual(temp.breed, None)
        self.assertEqual(temp.mixed, None)
        self.assertEqual(temp.age, None)
        self.assertEqual(temp.sex, None)
        self.assertEqual(temp.size, None)
        self.assertEqual(temp.org_id, None)
        self.assertEqual(temp.images_id, None)

    def test_adoptable_3 (self) :
        temp = Adoptable(name='the', breed='cat', mixed='in', age=111, sex='the', size='hat', org_id=222, images_id=333)
        self.assertEqual(temp.name, 'the')
        self.assertEqual(temp.breed, 'cat')
        self.assertEqual(temp.mixed, 'in')
        self.assertEqual(temp.age, 111)
        self.assertEqual(temp.sex, 'the')
        self.assertEqual(temp.size, 'hat')
        self.assertEqual(temp.org_id, 222)
        self.assertEqual(temp.images_id, 333)

    def test_breed_1 (self) :
        temp = Breed(name='a', types='b', personality='c', hairLength=1, weight=2, description='f', origin = 'g', temperament = 'h', shedding = 'i', grooming = 'j', recognitions = 'k', wikiLink = 'l', org_id = 3, images_id = 4)
        self.assertEqual(temp.name, 'a')
        self.assertEqual(temp.types, 'b')
        self.assertEqual(temp.personality, 'c')
        self.assertEqual(temp.hairLength, 1)
        self.assertEqual(temp.weight, 2)
        self.assertEqual(temp.description, 'f')
        self.assertEqual(temp.origin, 'g')
        self.assertEqual(temp.temperament, 'g')
        self.assertEqual(temp.shedding, 'i')
        self.assertEqual(temp.grooming, 'j')
        self.assertEqual(temp.recognitions, 'k')
        self.assertEqual(temp.wikiLink, 'l')
        self.assertEqual(temp.org_id, 3)
        self.assertEqual(temp.images_id, 4)


    def test_breed_2 (self) :
        temp = Breed()
        self.assertEqual(temp.name, None)
        self.assertEqual(temp.types, None)
        self.assertEqual(temp.personality, None)
        self.assertEqual(temp.hairLength, None)
        self.assertEqual(temp.weight, None)
        self.assertEqual(temp.description, None)
        self.assertEqual(temp.origin, None)
        self.assertEqual(temp.temperament, None)
        self.assertEqual(temp.shedding, None)
        self.assertEqual(temp.grooming, None)
        self.assertEqual(temp.recognitions, None)
        self.assertEqual(temp.wikiLink, None)
        self.assertEqual(temp.org_id, None)
        self.assertEqual(temp.images_id, None)

    def test_breed_3 (self) :
        temp = Breed(name='the', types='cat', personality='in', hairLength=111, weight=222, description='the', origin = 'hat', temperament = 'is', shedding = 'not', grooming = 'very', recognitions = 'smart', wikiLink = 'today', org_id = 333, images_id = 444)
        self.assertEqual(temp.name, 'the')
        self.assertEqual(temp.types, 'cat')
        self.assertEqual(temp.personality, 'in')
        self.assertEqual(temp.hairLength, 111)
        self.assertEqual(temp.weight, 222)
        self.assertEqual(temp.description, 'the')
        self.assertEqual(temp.origin, 'hat')
        self.assertEqual(temp.temperament, 'is')
        self.assertEqual(temp.shedding, 'not')
        self.assertEqual(temp.grooming, 'very')
        self.assertEqual(temp.recognitions, 'smart')
        self.assertEqual(temp.wikiLink, 'today')
        self.assertEqual(temp.org_id, 333)
        self.assertEqual(temp.images_id, 444)

    def test_organization_1 (self) :
        temp = Breed(name='a', address1='b', address2='c', city='d', state='e', description='f', zip = 1, country = 'g', phone = 2, fax = 3, email = 'h', latitude = 4.0, longitude = 5.0, org_id = 6, images_id = 7)
        self.assertEqual(temp.name, 'a')
        self.assertEqual(temp.address1, 'b')
        self.assertEqual(temp.address2, 'c')
        self.assertEqual(temp.city, 'd')
        self.assertEqual(temp.state, 'e')
        self.assertEqual(temp.description, 'f')
        self.assertEqual(temp.zip, 1)
        self.assertEqual(temp.country, 'g')
        self.assertEqual(temp.phone, 2)
        self.assertEqual(temp.fax, 3)
        self.assertEqual(temp.email, 'h')
        self.assertEqual(temp.latitude, 4.0)
        self.assertEqual(temp.longitude, 5.0)
        self.assertEqual(temp.org_id, 6)
        self.assertEqual(temp.images_id, 7)

    def test_organization_2 (self) :
        temp = Breed()
        self.assertEqual(temp.name, None)
        self.assertEqual(temp.address1, None)
        self.assertEqual(temp.address2, None)
        self.assertEqual(temp.city, None)
        self.assertEqual(temp.state, None)
        self.assertEqual(temp.description, None)
        self.assertEqual(temp.zip, None)
        self.assertEqual(temp.country, None)
        self.assertEqual(temp.phone, None)
        self.assertEqual(temp.fax, None)
        self.assertEqual(temp.email, None)
        self.assertEqual(temp.latitude, None)
        self.assertEqual(temp.longitude, None)
        self.assertEqual(temp.org_id, None)
        self.assertEqual(temp.images_id, None)

    def test_organization_3 (self) :
        temp = Breed(name='the', address1='cat', address2='in', city='the', state='hat', description='is', zip = 1, country = 'not', phone = 2, fax = 3, email = 'nice', latitude = 4.0, longitude = 5.0, org_id = 6, images_id = 7)
        self.assertEqual(temp.name, 'the')
        self.assertEqual(temp.address1, 'cat')
        self.assertEqual(temp.address2, 'in')
        self.assertEqual(temp.city, 'the')
        self.assertEqual(temp.state, 'hat')
        self.assertEqual(temp.description, 'is')
        self.assertEqual(temp.zip, 1)
        self.assertEqual(temp.country, 'not')
        self.assertEqual(temp.phone, 2)
        self.assertEqual(temp.fax, 3)
        self.assertEqual(temp.email, 'nice')
        self.assertEqual(temp.latitude, 4.0)
        self.assertEqual(temp.longitude, 5.0)
        self.assertEqual(temp.org_id, 6)
        self.assertEqual(temp.images_id, 7)

	# ---------
	# Adoptable
	# ---------

	def test_model_adoptable_1(self):
		mockResponse = {'Aatrox': {'name': 'Aatrox', 'title': 'the Darkin Blade'},
						'Thresh': {'name': 'Thresh', 'partype': 'Mana'} }
		self.assertEqual(mockResponse['Aatrox']['name'], 'Aatrox') 
		self.assertEqual(mockResponse['Aatrox']['title'], 'the Darkin Blade') 
		self.assertEqual(mockResponse['Thresh']['name'], 'Thresh') 
		self.assertEqual(mockResponse['Thresh']['partype'], 'Mana') 

		mockResponse = {'Aatrox': {'name': 'Aatrox', 'title': 'the Darkin Blade'},
						'Thresh': {'name': 'Thresh', 'partype': 'Mana'} }
		self.assertEqual(mockResponse['Aatrox']['name'], 'Aatrox') 
		self.assertEqual(mockResponse['Aatrox']['title'], 'the Darkin Blade') 
		self.assertEqual(mockResponse['Thresh']['name'], 'Thresh') 
		self.assertEqual(mockResponse['Thresh']['partype'], 'Mana') 

	def test_model_champions_2(self):
		mockChampion = Champion('Aatrox', 266, '', '', '', 'the Darkin Blade', 8, 4, 3,\
			4, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.assertEqual(mockChampion.name, 'Aatrox') 
		self.assertEqual(mockChampion.championId, 266) 
		self.assertEqual(mockChampion.title, 'the Darkin Blade') 

	def test_model_champions_3(self):
		champ1 = Champion.query.get(266)
		champ2 = Champion.query.get(412)
		self.assertEqual(champ1.name, 'Aatrox') 
		self.assertEqual(champ1.title, 'the Darkin Blade') 
		self.assertEqual(champ2.name, 'Thresh') 
		self.assertEqual(champ2.partype, 'Mana') 

	def test_model_champions_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/266')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], 'Aatrox') 
		self.assertEqual(jsonResponse['title'], 'the Darkin Blade') 

	'''
	# ---------
	# Champions
	# ---------

	def test_model_champions_1(self):
		mockResponse = {'Aatrox': {'name': 'Aatrox', 'title': 'the Darkin Blade'},
						'Thresh': {'name': 'Thresh', 'partype': 'Mana'} }
		self.assertEqual(mockResponse['Aatrox']['name'], 'Aatrox') 
		self.assertEqual(mockResponse['Aatrox']['title'], 'the Darkin Blade') 
		self.assertEqual(mockResponse['Thresh']['name'], 'Thresh') 
		self.assertEqual(mockResponse['Thresh']['partype'], 'Mana') 

	def test_model_champions_2(self):
		mockChampion = Champion('Aatrox', 266, '', '', '', 'the Darkin Blade', 8, 4, 3,\
			4, '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.assertEqual(mockChampion.name, 'Aatrox') 
		self.assertEqual(mockChampion.championId, 266) 
		self.assertEqual(mockChampion.title, 'the Darkin Blade') 

	def test_model_champions_3(self):
		champ1 = Champion.query.get(266)
		champ2 = Champion.query.get(412)
		self.assertEqual(champ1.name, 'Aatrox') 
		self.assertEqual(champ1.title, 'the Darkin Blade') 
		self.assertEqual(champ2.name, 'Thresh') 
		self.assertEqual(champ2.partype, 'Mana') 

	def test_model_champions_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/champions/266')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertEqual(jsonResponse['name'], 'Aatrox') 
		self.assertEqual(jsonResponse['title'], 'the Darkin Blade') 

	# ---------
	# Abilities
	# ---------

	def test_model_abilities_1(self):
		mockResponse = {'0': {'name': 'Dark Flight', 'maxrank': 5},
						'1': {'name': 'Blades of Torment', 'costType': 'pofcurrentHealth'} }
		self.assertEqual(mockResponse['0']['name'], 'Dark Flight') 
		self.assertEqual(mockResponse['0']['maxrank'], 5) 
		self.assertEqual(mockResponse['1']['name'], 'Blades of Torment') 
		self.assertEqual(mockResponse['1']['costType'], 'pofcurrentHealth')

	def test_model_abilities_2(self):
		mockAbility = ChampionAbility('Dark Flight', '', '', '', 5, '', '')
		self.assertEqual(mockAbility.name, 'Dark Flight') 
		self.assertEqual(mockAbility.maxrank, 5) 

	def test_model_abilities_3(self):
		ability1 = ChampionAbility.query.get(1)
		ability2 = ChampionAbility.query.get(2)
		self.assertTrue(ability1.name)
		self.assertTrue(ability1.maxrank)
		self.assertTrue(ability2.name)
		self.assertTrue(ability2.costType)

	def test_model_abilities_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/abilities/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['name'])
		self.assertTrue(jsonResponse['maxrank']) 

	# --------------
	# Featured Games
	# --------------

	def test_model_featuredgames_1(self):
		mockResponse = [{'gameLength': 321, 'game_mode': 'CLASSIC'},
						{'game_type': 'MATCHED_GAME', 'mapId': 11} ]
		self.assertEqual(mockResponse[0]['gameLength'], 321) 
		self.assertEqual(mockResponse[0]['game_mode'], 'CLASSIC') 
		self.assertEqual(mockResponse[1]['game_type'], 'MATCHED_GAME') 
		self.assertEqual(mockResponse[1]['mapId'], 11) 

	def test_model_featuredgames_2(self):
		mockGame = FeaturedGame(0, 321, 'CLASSIC', 0, '', 0)
		self.assertEqual(mockGame.gameLength, 321) 
		self.assertEqual(mockGame.game_mode, 'CLASSIC') 

	def test_model_featuredgames_3(self):
		game1 = FeaturedGame.query.get(1)
		game2 = FeaturedGame.query.get(2)
		self.assertTrue(game1.gameLength) 
		self.assertTrue(game1.champions) 
		self.assertTrue(game2.summoners)
		self.assertTrue(game2.mapId) 

	def test_model_featuredgames_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/featured-games/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['gameLength'])
		self.assertTrue(jsonResponse['champions'])

	# ---------
	# Summoners
	# ---------

	def test_model_summoners_1(self):
		mockResponse = {'Riesig': {'name': 'Riesig', 'profileIconId': 538},
						'GochuHunter': {'summonerLevel': 30, 'teamId': 100} }
		self.assertEqual(mockResponse['Riesig']['name'], 'Riesig') 
		self.assertEqual(mockResponse['Riesig']['profileIconId'], 538) 
		self.assertEqual(mockResponse['GochuHunter']['summonerLevel'], 30) 
		self.assertEqual(mockResponse['GochuHunter']['teamId'], 100) 

	def test_model_summoners_2(self):
		mockSummoner = Summoner(0, 'Riesig', 538, 30, False)
		self.assertEqual(mockSummoner.name, 'Riesig') 
		self.assertEqual(mockSummoner.profileIconId, 538) 

	def test_model_summoners_3(self):
		summoner1 = Summoner.query.get(1)
		summoner2 = Summoner.query.get(2)
		self.assertTrue(summoner1.name)
		self.assertTrue(summoner1.profileIconId) 
		self.assertTrue(summoner2.summonerLevel)
		self.assertTrue(summoner2.name)

	def test_model_summoners_4(self):
		apiResponse = urlopen('http://hardcarry.me/api/summoners/1')
		apiResponseInfo = apiResponse.info()
		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
		jsonResponse = json.loads(apiResponseRaw)
		self.assertTrue(jsonResponse['name'])
		self.assertTrue(jsonResponse['profileIconId'])
	'''

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
    unittest.main()
