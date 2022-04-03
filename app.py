# -*- coding: utf-8 -*-


from fastapi import FastAPI
from utils.log_events import LogEvents
from db.redis import RedisProxy
from config import Config
import api


class App(FastAPI):
    def __init__(self, config: Config):
        super().__init__()
        self._cfg = config
        LogEvents.info.init()

        self.add_event_handler("startup", self.startup)
        self.add_event_handler("shutdown", self.shutdown)
        LogEvents.info.event_handlers_added()


        self.include_router(api.router)
        LogEvents.info.api_added()


    async def startup(self) -> None:
        LogEvents.debug.startup_started()
        LogEvents.debug.startup_finished()


    async def shutdown(self) -> None:
        LogEvents.debug.shutdown_started()
        LogEvents.debug.shutdown_finished()
