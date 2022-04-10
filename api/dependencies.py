import config
from db import utils
from pymongo import MongoClient
from pymongo.database import Database


cfg = config.get_config()


def get_db_session() -> MongoClient:
    return utils.get_db_session(cfg.db)

def get_db() -> Database:
    return get_db_session().get_database(cfg.db.db)



