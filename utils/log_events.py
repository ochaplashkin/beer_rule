from dataclasses import dataclass
import logging

log = logging.getLogger()


@dataclass
class LogEventsDebug:
    startup_started: callable = lambda: log.debug("Startup handler started")
    startup_finished: callable = lambda: log.debug("Startup handler finished")

    shutdown_started: callable = lambda: log.debug("Shutdown handler started")
    shutdown_finished: callable = lambda: log.debug("Shutdown handler finished")


@dataclass
class LogEventsInfo:
    init: callable = lambda: log.info("App has been started")
    event_handlers_added: callable = lambda: log.info("Startup and shutdown handlers has been added")
    api_added: callable = lambda: log.info("API routes has been added")


@dataclass
class LogEvents:
    info: LogEventsInfo = LogEventsInfo()
    debug: LogEventsDebug = LogEventsDebug()
