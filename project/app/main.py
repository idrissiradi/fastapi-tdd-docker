import logging
import os

from fastapi import FastAPI

from app.api import ping
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application():
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


init_db(app)
