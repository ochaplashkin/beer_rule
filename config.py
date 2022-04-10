from dataclasses import dataclass
from email.policy import default
from functools import lru_cache
from configparser import ConfigParser

@dataclass(frozen=True)
class AppConfig:
    host: str
    port: str

@dataclass(frozen=True)
class DbConfig:
    host: str
    port: str
    usr: str
    pwd: str
    db: str

@dataclass(frozen=True)
class Config:
    app: AppConfig
    db: DbConfig


@lru_cache
def get_config(path: str = "config.ini"):
    config = ConfigParser()
    config.read(path)

    cfg_app = config["app"]
    cfg_db = config["db"]

    return Config(
        app=AppConfig(
            host=cfg_app['host'],
            port=int(cfg_app['port'])
        ),
        db=DbConfig(
            host=cfg_db['host'],
            port=cfg_db['port'],
            usr=cfg_db['usr'],
            pwd=cfg_db['pwd'],
            db=cfg_db['db']
        )
    )
