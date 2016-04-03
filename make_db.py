#!/usr/bin/env python3

# -------
# imports
# -------

from api_calls import (get_adoptables_list, get_organizations_list, get_breeds_list, get_single_adoptable, get_single_breed)
from app import db, app, es
import models, re

# ----------
# Adoptables
# ----------

def create_adoptable(character_id):
    # name = Column(String(50))
    # breed = Column(String(50))
    # mixed = Column(String(50))
    # age = Column(Integer)
    # sex = Column(String(10))
    # size = Column(String(15))
    # org_id = Column(Integer, ForeignKey('organizations.id'))
    # images_id = Column(Integer, ForeignKey('images.id'))
    # # one to many relationship
    # organization = relationship("Organization", back_populates="adoptables")

    # cat = get_single_adoptable(character_id)['data']['results'][0]
    cat = get_single_adoptable(character_id)
    print(cat)

#     id = character['id']
#     name = character['name']
#     description = character['description']
#     thumbnail = character['thumbnail']['path'] + "/standard_fantastic." \
#                 + character['thumbnail']['extension']
#     url = character['resourceURI']
#
#     character_db = models.Characters(id = id,
#                               name = name,
#                               description = description,
#                               thumbnail = thumbnail,
#                               url = url)
#
#     db.session.add(character_db)
#     db.session.commit()
#
#     for comic_url in character['comics']['items']:
#         m = re.match(".+/(?P<comic_id>\d+)", comic_url['resourceURI'])
#         comic_db = models.Comics.query.get(m.group("comic_id"))
#         if comic_db is None:
#             comic = get_single_comic(m.group("comic_id"))['data']['results'][0]
#             comic_db = models.Comics(id = comic['id'],
#                                      title = comic['title'])
#             es.index('comics', 'comic', {'title': comic['title'], 'description': comic['description']}, id=comic['id'])
#         models.Characters.query.get(character_id).comics.append(comic_db)
#
#     for events_url in character['events']['items']:
#         m = re.match(".+/(?P<event_id>\d+)", events_url['resourceURI'])
#         event_db = models.Events.query.get(m.group("event_id"))
#         if event_db is None:
#             event = get_single_event(m.group("event_id"))['data']['results'][0]
#             event_db = models.Events(id = event['id'],
#                           title = event['title'])
#             es.index('events', 'event', {'title': event['title']}, id=event['id'])
#         models.Characters.query.get(character_id).events.append(event_db)
#
#     for series_url in character['series']['items']:
#         m = re.match(".+/(?P<series_id>\d+)", series_url['resourceURI'])
#         series_db = models.Series.query.get(m.group("series_id"))
#         if series_db is None:
#             serie = get_single_series(m.group("series_id"))['data']['results'][0]
#             series_db = models.Series(id = serie['id'],
#                           title = serie['title'])
#             es.index('series', 'serie', {'title': serie['title']}, id=serie['id'])
#         models.Characters.query.get(character_id).series.append(series_db)
#
#     # urls = []
#     # for character_url in character['urls']:
#     #     url_list.append(character_url)
#     db.session.commit()
#     es.index('characters', 'character', {'name': character_db.name, 'description': character_db.description}, id=character_db.id)
#     return models.Characters.query.get(character_id)
#
# def populate_character(character_id):
#     character = get_single_character(character_id)['data']['results'][0]
#
#     description = character['description']
#     thumbnail = character['thumbnail']['path'] + "/standard_fantastic." \
#                 + character['thumbnail']['extension']
#     url = character['resourceURI']
#
#     models.Characters.query.get(character_id).description = description
#     models.Characters.query.get(character_id).thumbnail = thumbnail
#     models.Characters.query.get(character_id).url = url
#
#     for comic_url in character['comics']['items']:
#         m = re.match(".+/(?P<comic_id>\d+)", comic_url['resourceURI'])
#         comic_db = models.Comics.query.get(m.group("comic_id"))
#         if comic_db is None:
#             comic = get_single_comic(m.group("comic_id"))['data']['results'][0]
#             comic_db = models.Comics(id = comic['id'],
#                                      title = comic['title'])
#             es.index('comics', 'comic', {'title': comic['title'], 'description': comic['description']}, id=comic['id'])
#         models.Characters.query.get(character_id).comics.append(comic_db)
#
#     for events_url in character['events']['items']:
#         m = re.match(".+/(?P<event_id>\d+)", events_url['resourceURI'])
#         event_db = models.Events.query.get(m.group("event_id"))
#         if event_db is None:
#             event = get_single_event(m.group("event_id"))['data']['results'][0]
#             event_db = models.Events(id = event['id'],
#                           title = event['title'])
#             es.index('events', 'event', {'title': event['title']}, id=event['id'])
#         models.Characters.query.get(character_id).events.append(event_db)
#
#     for series_url in character['series']['items']:
#         m = re.match(".+/(?P<series_id>\d+)", series_url['resourceURI'])
#         series_db = models.Series.query.get(m.group("series_id"))
#         if series_db is None:
#             serie = get_single_series(m.group("series_id"))['data']['results'][0]
#             series_db = models.Series(id = serie['id'],
#                           title = serie['title'])
#             es.index('series', 'serie', {'title': serie['title']}, id=serie['id'])
#         models.Characters.query.get(character_id).series.append(series_db)
#
#     # urls = []
#     # for character_url in character['urls']:
#     #     url_list.append(character_url)
#     db.session.commit()
#     es.index('characters', 'character', {'name':  models.Characters.query.get(character_id).name, 'description': description}, id=character_id)
#     return models.Characters.query.get(character_id)

# ------
# Comics
# ------
