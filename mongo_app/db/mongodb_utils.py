import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    logging.info("concectando mongo")
    #db.client = AsyncIOMotorClient(str(MONGODB_URL),
    #                               maxPoolSize=MAX_CONNECTIONS_COUNT,
    #                               minPoolSize=MIN_CONNECTIONS_COUNT)
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
    logging.info("concectando 1 mongo")


async def close_mongo_connection():
    logging.info("close mongo connection...")
    db.client.close()
    logging.info("close mongo connection")