import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# connet to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# get reference to the 'pendataan_penduduk' database
db = client.pendataan_penduduk

# get reference to the 'Provinsi' collection
provinsi_collection = db.Provinsi


# query by ObjectId
document_to_find = {"_id": ObjectId("65363ed53a0685c0ac931bad")}

# write an expression that retrieves the document matching the query constraint in the 'Provinsi' collection.
result = provinsi_collection.find_one(document_to_find)
pprint.pprint(result)

# close the client
client.close()