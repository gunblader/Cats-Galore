#!/usr/bin/env python3

# -------
# imports
# -------

from api_calls import (get_adoptables_list, get_organizations_list, get_breeds_list, get_single_adoptable, get_single_breed)
from models import (db, Adoptable, AdoptableBreed, Breed, BreedOrganization, Organization, AdoptableImage, BreedImage)
import models, re
import xml.etree.ElementTree as etree
import xml.sax


db.drop_all()
db.create_all()



# ----------
# Adoptables
# ----------

def create_adoptable(character_id):
    cat = get_single_adoptable(character_id)
    data = cat['petfinder']['pet']
    catId = data['id']['$t']

    adoptable1 = Adoptable('Cali', 'no', 'Young', 'Female', 'Small', org1.id)
    db.session.add(adoptable1)
    image1 = AdoptableImage('http://www.catsgalore.me/static/images/model_images/Adoptable_Cali.jpg', adoptable1.id)
    db.session.add(image1)
    db.session.commit()

    print('Cat = ')
    print(data)
    print('Id of Cat = ')
    print(catId)
    return cat

def create_breed(name):
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
    print("root", r)
    return r

def create_organization(org):
    """
    Org parameter is a dictionary with info we need to use in database.
    """
    org1 = Organization("CatNAP", "", "", "Nanaimo", "BC", "", "VgV 1N3", "Canada", "", "", "", "", 0.0, 0.0)
    db.session.add(org1)
    db.session.commit()
    return True

def create_Breeds():
    """
    Enter information on all breeds into the database.
    """
    breeds = ["Abyssinian", "American Bobtail", "American Curl", "American Shorthair", "American Wirehair", "Australian Mist", "Balinese", "Bengal", "Birman", "Bombay", "British Longhair", "British Shorthair", "Burmese", "Burmilla", "California Spangled", "Chantilly", "Chartreux", "Chausie", "Chinese Li Hua Mao", "Colorpoint Shorthair", "Cornish Rex", "Cymric", "Devon Rex", "Donskoy", "Egyptian Mau", "European Burmese", "European Shorthair", "Exotic Shorthair", "German Rex", "Havana Brown", "Highlander", "Himalayan", "Japanese Bobtail", "Javanese", "Korats", "Kurilian Bobtail", "LaPerm", "Maine Coon", "Manx", "Minskin", "Munchkin", "Nebelung", "Norwegian Forest", "Ocicat", "Ojos Azules", "Oriental Longhair", "Oriental Shorthair", "Persian", "Peterbald", "Pixie‐Bob", "Ragamuffin", "Ragdoll", "Russian Blue", "Savannah", "Scottish Fold", "Selkirk Rex", "Serengeti", "Siamese Modern", "Siamese Traditional", "Siberian", "Singapura", "Snowshoe", "Sokoke", "Somali", "Sphynx", "Tiffanie", "Tonkinese", "Toyger", "Turkish Angora", "Turkish Van", "York Chocolate"]
    for breed in breeds:
        breed = breed.replace(" ", "%20")
        # x = create_breed(breed)
        # print(x)
        # breed1 = Breed('Abyssinian', 'natural', 'active | affectionate | agenda-driven | busy | curious | intelligent | interactive | loyal | playful | social', 'meadium | short', '7.5 to 16 lb (pounds)', 'Medium', 'Medium-sized and muscular cat with a ticked coat and the general appearance of a mountain lion | Coat appears iridescent due to its agouti ticking, with bands of color on each hair', 'Egypt', 'minimal', 'minimal', 'recognitions', 'wikiLink')
        # db.session.add(breed1)
        # image4 = BreedImage('http://www.catsgalore.me/static/images/model_images/Abyssinian.jpg', breed1.id
        # db.session.add(image4)
        # db.session.commit()

    print(breeds)
    return True

def create_Adoptables():

    return True

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
         print ("*****Image*****")
         self.pod = attributes["title"]
         print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Properties"):
         print ("*****Properties*****")
         self.pod = attributes["title"]
         print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Temperament"):
         print ("*****Temperament*****")
         self.pod = attributes["title"]
         print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Description"):
         print ("*****Description*****")
         self.pod = attributes["title"]
         print ("Title:", self.pod)
      elif (tag == "pod") and (attributes["title"] == "Wikipedia summary"):
         print ("*****Wikipedia summary*****")
         self.pod = attributes["title"]
         print ("Title:", self.pod)
      elif tag == "subpod":
          self.subpod = self.pod
          print ("Subpod:", self.subpod)
      elif tag == "plaintext":
          print ("**plaintext**")
      elif tag == "link":
          self.Wikipedia = attributes["url"]
          print ("**link**", self.Wikipedia)

   # Call when an elements ends
   def endElement(self, tag):
       if tag == "pod":
           if self.pod == "Image":
               print(self.image)
           elif self.pod == "History":
               print ("History:", self.History)
           elif self.pod == "Description":
               print ("Description:", self.Description)
           elif self.pod == "Properties":
               print ("Properties:", self.Properties)
           elif self.pod == "Image":
               print ("Image:", self.Image)
           elif self.pod == "Temperament":
               print ("Temperament:", self.Temperament)
           elif self.pod == "Wikipedia summary":
               print ("Wikipedia summary:", self.Wikipedia)

           print("clear")
           self.CurrentData = ""
           self.pod = ""

   # Call when a character is read
   def characters(self, content):
       if (self.CurrentData == "imagesource") and (self.pod == "Image"):
           self.image += " " + content
       elif (self.CurrentData == "plaintext") and (self.pod == "Temperament"):
           self.Temperament += " " + content
       elif (self.CurrentData == "plaintext") and (self.pod == "Properties"):
           self.Properties += " " + content
       elif (self.CurrentData == "plaintext") and (self.pod == "Description"):
           self.Description += " " + content
       elif (self.CurrentData == "plaintext") and (self.pod == "History"):
           self.History += " " + content

   # Call when you want the Json of data collected from XML
   def json(self):
       self.image = (self.image).replace("\n  ", "").replace("\n ", "").strip("   ")
       self.Properties = (self.Properties).replace("\n  ", "").replace("\n ", "").strip("   ")
       self.Description = (self.Description).replace("\n  ", "").replace("\n ", "").strip("   ")
       self.History = (self.History).replace("\n  ", "").replace("\n ", "").strip("   ")
       self.Temperament = (self.Temperament).replace("\n  ", "").replace("\n ", "").strip("   ")
       self.Wikipedia = (self.Wikipedia).replace("\n  ", "").replace("\n ", "").strip("   ")

       return {"image":self.image, "Properties":self.Properties, "Description":self.Description, "Temperament":self.Temperament, "Wikipedia":self.Wikipedia, "History":self.History}
