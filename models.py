from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Adoptable(Base):
    __tablename__ = 'adoptables'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    breed = Column(String(50))
    mixed = Column(String(50))
    age = Column(Integer)
    sex = Column(String(10))
    size = Column(String(15))
    org_id = Column(Integer, ForeignKey('organizations.id'))
    images_id = Column(Integer, ForeignKey('images.id'))
    # one to many relationship
    organization = relationship("Organization", back_populates="adoptables")
    # many to many relationship
    addresses = relationship("Address", back_populates='user',
                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

class Breed(Base):
    __tablename__ = 'breeds'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    types = Column(String(50))
    personality = Column(String(50))
    hairLength = Column(Integer)
    weight = Column(Integer)
    description = Column(String(500))
    origin = Column(String(50))
    temperament = Column(String(25))
    shedding = Column(String(50))
    grooming = Column(String(50))
    recognitions = Column(String(50))
    wikiLink = Column(String(50))
    org_id = Column(Integer, ForeignKey('organizations.id'))
    images_id = Column(Integer, ForeignKey('images.id'))

    organization = relationship("Organization", back_populates="addresses")
    addresses = relationship("Address", back_populates='user',
                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)


class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    address1 = Column(String(50))
    address2 = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    description = Column(String(500))
    zip = Column(Integer)
    country = Column(String(50))
    phone = Column(Integer)
    fax = Column(Integer)
    email = Column(String(50))
    latitude = Column(Decimal)
    longitude = Column(Decimal)
    org_id = Column(Integer, ForeignKey('organizations.id'))
    images_id = Column(Integer, ForeignKey('images.id'))

    # many to one relationship
    adoptables = relationship("Adoptable", back_populates="organization")
    # many to many relationship
    addresses = relationship("Address", back_populates='user',
                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)
