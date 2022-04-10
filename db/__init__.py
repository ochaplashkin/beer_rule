from pymongo import MongoClient

from config import DbConfig


def initialize(connect: MongoClient, cfg: DbConfig):
    return connect.get_database(cfg.db)

def terminate(connect: MongoClient, cfg: DbConfig):
    return connect.drop_database(cfg.db)
