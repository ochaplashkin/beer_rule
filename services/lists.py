# from models import list
from db import utils
from db import lists as db_lists
from pymongo.database import Database
from models.list import List, ListInput
from bson.objectid import ObjectId

COLLECTION_NAME: str = 'lists'

def initialize(db: Database):
    utils.create_collection(db, COLLECTION_NAME)
    db_lists.create_list(db, COLLECTION_NAME, {"name": "a"})


def create_list(db: Database, raw: ListInput):
    return List(
        id = str(db_lists.create_list(db, COLLECTION_NAME, raw.dict())),
        name = raw.name
    )

def read_list(db: Database, list_id: str):
    res = db_lists.read_list(db, COLLECTION_NAME, ObjectId(list_id))
    return List(
        id = str(res['_id']),
        name = res['name']
    )

def read_all_lists(db: Database):

    def to_model(raw_list) -> List:
        return List(
            id = str(raw_list['_id']),
            name = raw_list['name']
        )

    return list(map(
        lambda x: to_model(x),
        db_lists.read_all_lists(db, COLLECTION_NAME)
    ))

def delete_list(db: Database, list_id: str):
    res = db_lists.delete_list(db, COLLECTION_NAME, ObjectId(list_id))
    return List(
        id = str(res['_id']),
        name = res['name']
    )


def update_list(db: Database, list_id: str, raw: ListInput):
    def to_model(raw_list) -> List:
        return List(
            id = str(raw_list['_id']),
            name = raw_list['name']
        )
    return to_model(db_lists.update_list(db, COLLECTION_NAME, ObjectId(list_id), raw.dict()))

