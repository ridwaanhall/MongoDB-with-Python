import os

from dotenv import load_dotenv
from pymongo import MongoClient

# load config from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")


client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)
    
client.close()