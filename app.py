# -*- coding: utf-8 -*-


from fastapi import FastAPI
from config import Config, DbConfig
from utils.log_events import LogEvents
import api
from db import utils as db_utils
import db
from services import lists as lists_service

class App(FastAPI):
    def __init__(self, config):
        super().__init__()
        LogEvents.info.init()

        self._cfg: Config = config

        self.add_event_handler("startup", self.startup)
        self.add_event_handler("shutdown", self.shutdown)
        LogEvents.info.event_handlers_added()


        self.include_router(api.router)
        LogEvents.info.api_added()
    
    @property
    def db_config(self) -> DbConfig:
        return self._cfg.db
    
    @property
    def app_config(self) -> DbConfig:
        return self._cfg.app


    async def startup(self) -> None:
        LogEvents.debug.startup_started()

        connect = db_utils.get_db_session(self.db_config)
        db_ = db.initialize(connect,  self.db_config)
        lists_service.initialize(db_)

        LogEvents.debug.startup_finished()


    async def shutdown(self) -> None:
        LogEvents.debug.shutdown_started()

        connect = db_utils.get_db_session(self.db_config)
        db.terminate(connect, self.db_config)
        
        LogEvents.debug.shutdown_finished()
