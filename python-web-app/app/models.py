from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

"""
Adoptable Class representation
"""
class Adoptable(db.Model):
    __tablename__ = 'adoptables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mixed = db.Column(db.String(100))
    age = db.Column(db.String(100))
    sex = db.Column(db.String(10))
    size = db.Column(db.String(15))
    org_id = db.Column(db.Integer, ForeignKey('organizations.id'))


    # # one to many relationship
    # organization = db.relationship("Organization", back_populates="adoptables")
    # # many to many relationship
    # addresses = db.relationship("Address", back_populates='user',
    #                  cascade="all, delete, delete-orphan")

    def __init__(self, name, mixed, age, sex, size, org_id):
        self.name = name
        self.mixed = mixed
        self.age = age
        self.sex = sex
        self.size = size
        self.org_id = org_id

    def __repr__(self):
        return "<Adoptable(name='%s')>" % (self.name)


class AdoptableBreed(db.Model):
    __tablename__ = 'adobtableBreeds'
    id = db.Column(db.Integer, primary_key=True)
    adoptable_id = db.Column(db.Integer, ForeignKey('adoptables.id'))
    breed_id = db.Column(db.Integer, ForeignKey('breeds.id'))

    def __init__(self, adoptable_id, breed_id):
        self.adoptable_id = adoptable_id
        self.breed_id = breed_id

    def __repr__(self):
        return "<AdoptableBreed(Adoptable ID='%s', Breed ID='%s')>" % (self.adoptable_id, self.breed_id)


class Breed(db.Model):
    __tablename__ = 'breeds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    types = db.Column(db.String(100))
    personality = db.Column(db.String(5000))
    hairLength = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    size = db.Column(db.String(100))
    description = db.Column(db.String(5000))
    origin = db.Column(db.String(100))
    shedding = db.Column(db.String(100))
    grooming = db.Column(db.String(100))
    recognitions = db.Column(db.String(100))
    wikiLink = db.Column(db.String(1100))

    # organization = relationship("Organization", back_populates="addresses")
    # addresses = relationship("Address", back_populates='user',
    #                  cascade="all, delete, delete-orphan")

    def __init__(self, name, types, personality, hairLength, weight, size, description, origin, shedding, grooming, recognitions, wikiLink):
        self.name = name
        self.types = types
        self.personality = personality
        self.hairLength = hairLength
        self.weight = weight
        self.size = size
        self.description = description
        self.origin = origin
        self.shedding = shedding
        self.grooming = grooming
        self.recognitions = recognitions
        self.wikiLink = wikiLink

    def __repr__(self):
        return "<Breed(name='%s')>" % (self.password)

class BreedOrganization(db.Model):
    __tablename__ = 'breedOrganizations'
    id = db.Column(db.Integer, primary_key=True)
    breed_id = db.Column(db.Integer, ForeignKey('breeds.id'))
    organization_id = db.Column(db.Integer, ForeignKey('organizations.id'))

    def __init__(self, breed_id, organization_id):
        self.breed_id = breed_id
        self.organization_id = organization_id

    def __repr__(self):
        return "<breedOrganization(Breed ID='%s', Organization ID='%s')>" % (self.breed_id, self.organization_id)

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address1 = db.Column(db.String(60))
    address2 = db.Column(db.String(60))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    description = db.Column(db.String(500))
    postalCode = db.Column(db.String(100))
    country = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    fax = db.Column(db.String(100))
    email = db.Column(db.String(80))
    url = db.Column(db.String(300))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # # many to one relationship
    # adoptables = relationship("Adoptable", back_populates="organization")
    # # many to many relationship
    # addresses = relationship("Address", back_populates='user',
    #                  cascade="all, delete, delete-orphan")

    def __init__(self, name, address1, address2, city, state, description, postalCode, country, phone, fax, email, url, latitude, longitude):
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.description = description
        self.postalCode = postalCode
        self.country = country
        self.phone = phone
        self.fax = fax
        self.email = email
        self.url = url
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<Organization(name='%s')>" % (self.name)


class AdoptableImage(db.Model):
    __tablename__ = 'adoptableImages'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    adoptable_id = db.Column(db.Integer, ForeignKey('adoptables.id'))

    def __init__(self, url, adoptable_id):
        self.url = url
        self.adoptable_id = adoptable_id

    def __repr__(self):
        return "<Image(url='%s')>" % (self.url)

class BreedImage(db.Model):
    __tablename__ = 'breedImages'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    breed_id = db.Column(db.Integer, ForeignKey('breeds.id'))

    def __init__(self, url, breed_id):
        self.url = url
        self.breed_id = breed_id

    def __repr__(self):
        return "<Image(url='%s')>" % (self.url)
