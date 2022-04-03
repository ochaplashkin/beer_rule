import redis
from config import RedisConfig


class RedisProxy(redis.Redis):
    def __init__(self, cfg: RedisConfig):
        super().__init__(
            host=cfg.host,
            port=cfg.port,
            db=0
        )
