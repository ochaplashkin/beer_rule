from typing import Union
from unittest.mock import DEFAULT
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from config import DbConfig
from urllib.parse import quote_plus
from functools import lru_cache
from db import lists


@lru_cache
def get_db_session(cfg: DbConfig) -> MongoClient:
    uri: str = "mongodb://%s:%s@%s:%s" % (
        quote_plus(cfg.usr),
        quote_plus(cfg.pwd),
        quote_plus(cfg.host),
        quote_plus(cfg.port)
    )
    return MongoClient(uri)

def create_db(client: MongoClient, db_name: str):
    return client.get_database(db_name)

def drop_db(client: MongoClient, db: Union[Database, str]):
    return client.drop_database(db)

def create_collection(db: Database, collection_name: str):
    return db.get_collection(collection_name)

def drop_collection(db: Database, collection_name: str):
    return db.drop_collection(collection_name)


