#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from models import Adoptable, Breed, Organization

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def adoptable_test_1 (self) :
        temp = Adoptable(name='a', breed='b', mixed='c', age=1, sex='e', size='f', org_id=2, images_id=3)
        self.assertEqual(temp.name, 'a')
        self.assertEqual(temp.breed, 'b')
        self.assertEqual(temp.mixed, 'c')
        self.assertEqual(temp.age, 1)
        self.assertEqual(temp.sex, 'e')
        self.assertEqual(temp.size, 'f')
        self.assertEqual(temp.org_id, 2)
        self.assertEqual(temp.images_id, 3)

    def adoptable_test_2 (self) :
        temp = Adoptable()
        self.assertEqual(temp.name, None)
        self.assertEqual(temp.breed, None)
        self.assertEqual(temp.mixed, None)
        self.assertEqual(temp.age, None)
        self.assertEqual(temp.sex, None)
        self.assertEqual(temp.size, None)
        self.assertEqual(temp.org_id, None)
        self.assertEqual(temp.images_id, None)

    def adoptable_test_3 (self) :
        temp = Adoptable(name='the', breed='cat', mixed='in', age=111, sex='the', size='hat', org_id=222, images_id=333)
        self.assertEqual(temp.name, 'the')
        self.assertEqual(temp.breed, 'cat')
        self.assertEqual(temp.mixed, 'in')
        self.assertEqual(temp.age, 111)
        self.assertEqual(temp.sex, 'the')
        self.assertEqual(temp.size, 'hat')
        self.assertEqual(temp.org_id, 222)
        self.assertEqual(temp.images_id, 333)

    def breed_test_1 (self) :
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


    def breed_test_2 (self) :
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

    def breed_test_3 (self) :
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

    def organization_test_1 (self) :
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

    def organization_test_2 (self) :
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

    def organization_test_3 (self) :
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

# ----
# main
# ----

if __name__ == "__main__" :
    main()