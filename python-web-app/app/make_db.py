#!/usr/bin/env python

# -------
# imports
# -------

from api_calls import (get_adoptables_list, get_organizations_list, get_single_adoptable, get_single_breed)
# from api_calls import (get_adoptables_list, get_organizations_list, get_breeds_list, get_single_adoptable, get_single_breed)
from models import (db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage)
import models, re
import xml.etree.ElementTree as etree
import xml.sax


# ----------
# Adoptables
# ----------

def create_adoptable(character_id):
    """
    'character_id' parameter is an id of a adoptable cat listed in Pet Finder.
    Makes call to pet finder Api to get cat's info and commits it to our database
    Attributes: name, breed, mixed, age, sex, size
    """
    name = ""
    breed = []
    mixed = ""
    age = ""
    sex = ""
    size = ""
    description = ""
    orgID = ""
    org = {}

    cat = get_single_adoptable(character_id)
    data = cat['petfinder']['pet']

    # Passes data to create an entry in Organization Table
    org_data = data['contact']
    if "address1" in org_data:
        org['address1'] = org_data['address1']
        if '$t' in org['address1']:
            org['address1'] = org['address1']['$t']
    else:
        org['address1'] = "N/A"
    if "address2" in org_data:
        org['address2'] = org_data['address2']
        if '$t' in org['address2']:
            org['address2'] = org['address2']['$t']
    else:
        org['address2'] = "N/A"
    if "city" in org_data:
        org['city'] = org_data['city']
        if '$t' in org['city']:
            org['city'] = org['city']['$t']
    else:
        org['city'] = "N/A"
    if "state" in org_data:
        org['state'] = org_data['state']
        if '$t' in org['state']:
            org['state'] = org['state']['$t']
    else:
        org['state'] = "N/A"
    if "description"in org_data:
        org['description'] = org_data['description']
        if '$t' in org['description']:
            org['description'] = org['description']['$t']
    else:
        org['description'] = "N/A"
    if "zip" in org_data:
        org['zip'] = org_data['zip']
        if '$t' in org['zip']:
            org['zip'] = org['zip']['$t']
    else:
        org['zip'] = "N/A"
    if "country" in org_data:
        org['country'] = org_data['country']
        if '$t' in org['country']:
            org['country'] = org['country']['$t']
    else:
        org['country'] = "N/A"
    if "phone" in org_data:
        org['phone'] = org_data['phone']
        if '$t' in org['phone']:
            org['phone'] = org['phone']['$t']
    else:
        org['phone'] = "N/A"
    if "fax" in org_data:
        org['fax'] = org_data['fax']
        if '$t' in org['fax']:
            org['fax'] = org['fax']['$t']
    else:
        org['fax'] = "N/A"
    if "email"in org_data:
        org['email'] = org_data['email']
        if '$t' in org['email']:
            org['email'] = org['email']['$t']
    else:
        org['email'] = "N/A"
    if "latitude" in org_data:
        org['latitude'] = org_data['latitude']
        if '$t' in org['latitude']:
            org['latitude'] = org['latitude']['$t']
    else:
        org['latitude'] = "0"
    if "longitude" in org_data:
        org['longitude'] = org_data['longitude']
        if '$t' in org['longitude']:
            org['longitude'] = org['longitude']['$t']
    else:
        org['longitude'] = "0"
    if "name" in org_data:
        org['name'] = org_data['name']
        if '$t' in org['name']:
            org['name'] = org['name']['$t']
    else:
        org['name'] = org['email']

    # print('organization', org)
    orgID = create_organization(org)


    if "age" in data:
        age = data['age']
        if '$t' in age:
            age = age['$t']
    else:
        age = "N/A"
    if "size" in data:
        size = data['size']
        if '$t' in size:
            size = size['$t']
    else:
        age = "N/A"
    if "breeds" in data:
        breeds = data['breeds']['breed']
        # print type(breeds)
        if type(breeds) is dict:
            breed.append(breeds['$t'])
        else:
            for item in breeds:
                if '$t' in item:
                    breed.append(item['$t'])
                    print breed
    else:
        breed = []
    if "description" in data:
        description = data['description']
        if '$t' in description:
            description = description['$t']
    else:
        description = "N/A"
    if "mix" in data:
        mixed = data['mix']
        if '$t' in mixed:
            mixed = mixed['$t']
    else:
        mixed = "N/A"
    if "sex" in data:
        sex = data['sex']
        if '$t' in sex:
            sex = sex['$t']
    else:
        sex = "N/A"
    if "name" in data:
        name = data['name']
        if '$t' in name:
            name = name['$t']
    else:
        name = "N/A"


    # Adding to database starts here.
    # Makes Adoptable table entry
    adoptable1 = Adoptable(name, mixed, age, sex, size, orgID)
    db.session.add(adoptable1)
    db.session.commit()

    # Adding Pictures to Images table.
    media = data['media']
    if 'photos' in media:
        media = media['photos']['photo']
    # print ("photos = ", media)
    for pic in media:
        if "$t" in pic:
            picName = pic['$t']
        else:
            picName = "N/A"
        # print("pic = ", picName)

        # Add Pictures
        image1 = AdoptableImage(picName, adoptable1.id)
        db.session.add(image1)
        db.session.commit()

    #This dict is used to change breed names to fit those in our databases.
    a = {"Abyssinian":"Abyssinian", "American Curl":"American Curl", "American Shorthair":"American Shorthair", "American Wirehair":"American Wirehair", "Applehead Siamese":"Siamese Modern", "Balinese":"Balinese", "Bengal":"Bengal", "Birman":"Birman", "Bobtail":"Japanese Bobtail", "Bombay":"Bombay", "British Shorthair":"British Shorthair"}
    b = {"Burmese":"Burmese", "Burmilla":"Burmilla", "Calico":"California Spangled", "Canadian Hairless":"Sphynx", "Chartreux":"Chartreux", "Chausie":"Chausie", "Chinchilla":"Chausie", "Cornish Rex":"Cornish Rex"}
    c = {"Domestic Long Hair - brown":"British Longhair", "Domestic Long Hair - buff":"British Longhair", "Domestic Long Hair - buff and white":"British Longhair", "Domestic Long Hair - gray and white":"British Longhair", "Domestic Long Hair - orange":"British Longhair", "Domestic Long Hair - orange and white":"British Longhair", "Domestic Long Hair-black":"British Longhair", "Domestic Long Hair-black and white":"British Longhair", "Domestic Long Hair-gray":"British Longhair", "Domestic Long Hair-white":"British Longhair", "Domestic Medium Hair":"British Longhair", "Domestic Medium Hair - brown":"British Longhair"}
    d = {"Domestic Medium Hair - buff":"British Longhair", "Domestic Medium Hair - buff and white":"British Longhair", "Domestic Medium Hair - gray and white":"British Longhair", "Domestic Medium Hair - orange and white":"British Longhair", "Domestic Medium Hair-black":"British Longhair", "Domestic Medium Hair-black and white":"British Longhair", "Domestic Medium Hair-gray":"British Longhair", "Domestic Medium Hair-orange":"British Longhair", "Domestic Medium Hair-white":"British Longhair", "Domestic Short Hair":"British Longhair"}
    e = {"Domestic Short Hair - brown":"British Longhair", "Domestic Short Hair - buff":"British Longhair", "Exotic Shorthair":"Exotic Shorthair", "Extra-Toes Cat (Hemingway Polydactyl)":"Exotic Shorthair", "Havana":"Havana Brown", "Himalayan":"Himalayan"}
    f = {"Domestic Short Hair - buff and white":"British Longhair", "Domestic Short Hair - gray and white":"British Longhair", "Domestic Short Hair - orange and white":"British Longhair", "Domestic Short Hair-black":"British Longhair", "Domestic Short Hair-black and white":"British Longhair", "Domestic Short Hair-gray":"British Longhair", "Domestic Short Hair-mitted":"British Longhair", "Domestic Short Hair-orange":"British Longhair", "Domestic Short Hair-white":"British Longhair", "Egyptian Mau":"Egyptian Mau"}
    g = {"Japanese Bobtail":"Japanese Bobtail", "Javanese":"Javanese", "Korat":"Korats", "LaPerm":"LaPerm", "Maine Coon":"Maine Coon", "Manx":"Manx", "Munchkin":"Munchkin", "Nebelung":"Nebelung", "Norwegian Forest Cat":"Norwegian Forest", "Ocicat":"Ocicat"}
    h = {"Tonkinese":"Tonkinese", "Torbie":"Toyger", "Tortoiseshell":"Tiffanie", "Turkish Angora":"Turkish Angora", "Turkish Van":"Turkish Van", "Snowshoe":"Snowshoe", "Tuxedo":"Turkish Van"}
    i = {"Oriental Long Hair":"Oriental Longhair", "Oriental Short Hair":"Oriental Shorthair", "Oriental Tabby":"Oriental Shorthair", "Persian":"Persian", "Pixie-Bob":"Pixie Bob", "Ragamuffin":"Ragamuffin", "Ragdoll":"Ragdoll", "Russian Blue":"Russian Blue", "Scottish Fold":"Scottish Fold"}
    j = {"Somali":"Somali", "Sphynx (hairless cat)":"Sphynx", "Tabby":"Oriental Shorthair", "Tabby - black":"Oriental Shorthair", "Tabby - Brown":"Oriental Shorthair", "Tabby - buff":"Oriental Shorthair", "Tabby - Grey":"Oriental Shorthair", "Tabby - Orange":"Oriental Shorthair", "Tabby - white":"Oriental Shorthair", "Tiger":"Toyger"}
    k = {"Cymric":"Cymric", "Devon Rex":"Devon Rex", "Dilute Calico":"California Spangled", "Dilute Tortoiseshell":"Tiffanie", "Domestic Long Hair":"British Longhair", "Selkirk Rex":"Selkirk Rex", "Siamese":"Siamese Traditional", "Siberian":"Siberian", "Silver":"Scottish Fold", "Singapura":"Singapura"}
    petfinder = [a, b, c, d, f, g, h, i, j, k]


    ##print "breed = ", breed
    # Adding Relationships to adoptablebreed table.
    if breed != []:
        for item in breed:
            # print "name = ", item
            for x in petfinder:
                if item in x:
                    item = x[item]
                    break
            # print "Changed name = ", item
            exists = db.session.query(Breed).filter_by(name=item).order_by(Breed.id).first()
            # print ("exists = ", exists)
            if exists != None:
                # print "here = ",  exists.id
                # Add breed relationship
                breed1 = AdoptableBreed(adoptable1.id, exists.id)
                db.session.add(breed1)
                db.session.commit()


    return True

def create_breed(name):
    """
    Just gets info from wolfram alpha and parses the XML that is returns from api call.
    Then passes the info on as a Json.
    """
    # print("name: ", name)

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = BreedHandler()
    parser.setContentHandler( Handler )

    breed = get_single_breed(name)
    parser.parse(breed)
    r = Handler.json()

    # print("Parsed and returns Json = ", r)
    return r

def create_organization(org):
    """
    'Org' parameter is a dictionary with info we need to use in database.
    Attributes: name, address1, address2, city, state, description, zip,
    country, phone, fax, email, latitude, longitude
    """
    name = org['name'] or org['email']
    address1 = org['address1'] or "N/A"
    address2 = org['address2'] or "N/A"
    city = org['city'] or "N/A"
    state = org['state'] or "N/A"
    description = org['description'] or "N/A"
    zip = org['zip'] or "N/A"
    country = org['country'] or "N/A"
    phone = org['phone'] or "N/A"
    fax = org['fax'] or "N/A"
    email = org['email'] or "N/A"
    latitude = org['latitude'] or "N/A"
    longitude = org['longitude'] or "N/A"

    # Adding to database starts here.
    org1 = Organization(name, address1, address2, city, state, description, zip, country, phone, fax, email, latitude, longitude, 0)
    # Check to see if Organization already exists in Database.
    # print ("org =", org['email'])
    exists = db.session.query(Organization).filter_by(name=org['email']).order_by(Organization.id).first()
    # print ("exists = ", exists)
    if exists != None:
        # print "here = ",  exists.name
        if org1.name == exists.name:
            # print "here1 = ",  exists.id
            return exists.id
        else:
            # print "else"
            db.session.add(org1)
            db.session.commit()
            return org1.id
    else:
        # print "else"
        db.session.add(org1)
        db.session.commit()
        return org1.id

def dbCreate():
    db.configure_mappers()
    # db.create_all()

def create_Breeds():
    """
    Enter information on all breeds into the database.
    Attributes : name, types, personality, `hairlength`, weight, size,
    description, origin, shedding, grooming, recognitions, `wikilink`
    """
    # db.drop_all()
    # db.configure_mappers()
    db.create_all()

    name = ""
    types = ""
    personality = ""
    hairlength = ""
    weight = ""
    size = ""
    description = ""
    origin = ""
    temperament = ""
    shedding = ""
    grooming = ""
    recognitions = "N/A"
    wikilink = ""
    count = 0


    a = ["Abyssinian", "American Bobtail", "American Curl", "American Shorthair", "American Wirehair", "Australian Mist", "Balinese", "Bengal", "Birman", "Bombay", "British Longhair", "British Shorthair", "Burmese", "Burmilla", "California Spangled", "Chantilly", "Chartreux", "Chausie"]
    b = ["Chinese Li Hua Mao", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egyptian Mau", "European Burmese", "European Shorthair", "Exotic Shorthair", "German Rex", "Havana Brown", "Highlander", "Himalayan", "Japanese Bobtail", "Javanese", "Korats", "Kurilian Bobtail", "LaPerm"]
    c = ["Maine Coon", "Manx", "Minskin", "Munchkin", "Nebelung", "Norwegian Forest", "Ocicat", "Ojos Azules", "Oriental Longhair", "Oriental Shorthair", "Persian", "Peterbald", "Pixie Bob", "Ragamuffin", "Ragdoll", "Russian Blue", "Savannah", "Scottish Fold", "Selkirk Rex"]
    d = ["Serengeti", "Siamese Modern", "Siamese Traditional", "Siberian", "Singapura", "Snowshoe", "Sokoke", "Somali", "Sphynx", "Tiffanie", "Tonkinese", "Toyger", "Turkish Angora", "Turkish Van", "York Chocolate"]
    # breeds = [a, b, c, d]
    breeds = [a,[]]

    #Getting breed info starts here.
    for item in breeds:
        for breed in item:
            count += 1
            name = breed
            x = create_breed(breed.replace(" ", "%20"))
            description = x['Description']
            a = description.replace('\xe2\x80\x90'.decode('utf-8'), " ")
            # print description
            description = a
            temperament = x['Temperament']
            # print temperament
            wikilink = x['Wikipedia']
            # print wikilink
            # print("Properties =")
            info = x['Properties']
            for i in info:
                if "type of breed" in i:
                    types = i.replace("type of breed | ", "")
                    # print types
                elif "size" in i:
                    size = i.replace("size | ", "")
                    # print size
                elif "weight" in i:
                    weight = i.replace("weight | ", "")
                    # print weight
                elif "shedding" in i:
                    shedding = i.replace("shedding | ", "")
                    # print shedding
                elif "hair length" in i:
                    hairlength = i.replace("hair length | ", "")
                    # print hairlength
                elif "grooming" in i:
                    grooming = i.replace("grooming | ", "")
                    # print grooming
                elif "origin" in i:
                    origin = i.replace("origin | ", "")
                    # print origin

            # Adding to database starts here.
            breed1 = Breed(name, types, temperament, hairlength, weight, size, description, origin, shedding, grooming, recognitions, wikilink)
            db.session.add(breed1)
            db.session.commit()

            image1 = BreedImage(x['image'], breed1.id)
            db.session.add(image1)
            db.session.commit()

    # print("Breeds Done.")
    # print(count, " Created")
    return count

def create_Adoptables():
    count = 0
    a_list = get_adoptables_list()
    cats = a_list['petfinder']['pets']['pet']
    for cat in cats:
        count += 1
        create_adoptable(cat['id']['$t'])

    # print("Adoptables Done")
    # print(count, " Created")
    return count


class BreedHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.pod = ""
      self.subpod = ""
      self.image = ""
      self.Properties = ""
      self.Description = ""
      self.Temperament = ""
      self.Wikipedia = ""
      self.History = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if (tag == "pod") and (attributes["title"] == "Image") :
        #  print ("*****Image*****")
         self.pod = attributes["title"]
        #  print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Properties"):
        #  print ("*****Properties*****")
         self.pod = attributes["title"]
        #  print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Temperament"):
        #  print ("*****Temperament*****")
         self.pod = attributes["title"]
        #  print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Description"):
        #  print ("*****Description*****")
         self.pod = attributes["title"]
        #  print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Wikipedia summary"):
        #  print ("*****Wikipedia summary*****")
         self.pod = attributes["title"]
        #  print ("Title:", self.pod)
      elif tag == "subpod":
          self.subpod = self.pod
        #   print ("Subpod:", self.subpod)
      elif tag == "link":
          self.Wikipedia = attributes["url"]
        #   print ("**link**", self.Wikipedia)

   # Call when an elements ends
   def endElement(self, tag):
       if tag == "pod":
        #    if self.pod == "Image":
        #        print(self.image)
        #    elif self.pod == "History":
        #        print ("History:", self.History)
        #    elif self.pod == "Description":
        #        print ("Description:", self.Description)
        #    elif self.pod == "Properties":
        #        print ("Properties:", self.Properties)
        #    elif self.pod == "Image":
        #        print ("Image:", self.Image)
        #    elif self.pod == "Temperament":
        #        print ("Temperament:", self.Temperament)
        #    elif self.pod == "Wikipedia summary":
        #        print ("Wikipedia summary:", self.Wikipedia)
           #
        #    print("clear")
           self.CurrentData = ""
           self.pod = ""

   # Call when a character is read
   def characters(self, content):
       if (self.CurrentData == "imagesource") and (self.pod == "Image"):
           self.image += content
       elif (self.CurrentData == "plaintext") and (self.pod == "Temperament"):
           self.Temperament += content
       elif (self.CurrentData == "plaintext") and (self.pod == "Properties"):
           self.Properties += content
       elif (self.CurrentData == "plaintext") and (self.pod == "Description"):
           self.Description += content
       elif (self.CurrentData == "plaintext") and (self.pod == "History"):
           self.History += content

   # Call when you want the Json of data collected from XML
   def json(self):
       self.image = (self.image).replace("\n  ", "").replace("\n", "")
       self.Properties = (self.Properties).strip("   ").split("\n")
       self.Description = (self.Description).replace("\n  ", "").replace("\n", "")
       self.History = (self.History).replace("\n  ", "").replace("\n", "")
       self.Temperament = (self.Temperament).replace("\n  ", "").replace("\n", "")
       self.Wikipedia = (self.Wikipedia).replace("\n ", "").replace("\n", "")

       return {"image":self.image, "Properties":self.Properties, "Description":self.Description, "Temperament":self.Temperament, "Wikipedia":self.Wikipedia, "History":self.History}
