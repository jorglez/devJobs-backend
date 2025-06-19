from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from core.config import settings



client = MongoClient(settings.db_url, server_api=ServerApi('1'))

db = client[settings.db_name]

print(db)