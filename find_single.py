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
provinsi_collection = db.Desa


# query by ObjectId
document_to_find = {"_id": ObjectId("653648583ee1ca591bc986d9")}

# write an expression that retrieves the document matching the query constraint in the 'Provinsi' collection.
result = provinsi_collection.find_one(document_to_find)
pprint.pprint(result)

# close the client
client.close()