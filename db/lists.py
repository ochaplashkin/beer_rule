from typing import Union
from pymongo.collection import Collection
from bson import ObjectId
from pymongo.database import Database


def create_list(db: Database, c: str, list):
    return db.get_collection(c).insert_one(list).inserted_id

def read_list(db: Database, c: str, list_id: ObjectId):
    return db.get_collection(c).find_one({'_id': list_id})

def read_all_lists(db: Database, c: str):
    return list(db.get_collection(c).find())

def delete_list(db: Database, c: str, list_id: ObjectId):
    return db.get_collection(c).find_one_and_delete({'_id': list_id})

def update_list(db: Database, c: str, list_id: ObjectId, data:dict):
    return db.get_collection(c).find_one_and_update(
        {'_id': list_id},
        {'$set': data}
    )