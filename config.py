from dataclasses import dataclass
from functools import lru_cache
from configparser import ConfigParser

@dataclass
class AppConfig:
    host: str
    port: str

@dataclass
class Config:
    app: AppConfig


@lru_cache
def get_config(path: str = "config.ini"):
    config = ConfigParser()
    config.read(path)

    print(config)

    cfg_app = config["app"]

    return Config(
        app=AppConfig(
            host=cfg_app['host'],
            port=int(cfg_app['port'])
        )
    )
