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
#/////////////////////////////////////////////////////////////////////////////#
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    addresses = relationship("Address", back_populates='user',
                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

# make instance of mapped class
#      ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

class Address(Base):
     __tablename__ = 'addresses'
     id = Column(Integer, Sequence('address_id_seq'), primary_key=True)
     email_address = Column(String(255), nullable=False)
     user_id = Column(Integer, ForeignKey('users.id'))

     user = relationship("User", back_populates="addresses")

     def __repr__(self):
         return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

# make instance of mapped class and relationship
#     jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
#     jack.addresses    #this is [empty]

#     **** Add addresses now ****
#     jack.addresses = [
#                 Address(email_address='jack@google.com'),
#                 Address(email_address='j25@yahoo.com')]

class BlogPost(Base):
     __tablename__ = 'posts'

     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('users.id'))
     headline = Column(String(255), nullable=False)
     body = Column(Text)

     # many to many BlogPost<->Keyword
     keywords = relationship('Keyword',
                             secondary=post_keywords,
                             back_populates='posts')

     def __init__(self, headline, body, author):
         self.author = author
         self.headline = headline
         self.body = body

     def __repr__(self):
         return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)


 class Keyword(Base):
     __tablename__ = 'keywords'

     id = Column(Integer, primary_key=True)
     keyword = Column(String(50), nullable=False, unique=True)
     posts = relationship('BlogPost',
                          secondary=post_keywords,
                          back_populates='keywords')

     def __init__(self, keyword):
         self.keyword = keyword
