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


# Filter by ObjectId
document_to_update = {"_id": ObjectId("65363ed53a0685c0ac931bad")}

# update an expression that retrieves the document matching the query constraint in the 'Provinsi' collection.
add_to_update = {"$inc": {"id_provinsi": 10}}

# print original document
pprint.pprint(provinsi_collection.find_one(document_to_update))

# write an expression that retrieves the document matching the query constraint in the 'Provinsi' collection.
result = provinsi_collection.update_one(document_to_update, add_to_update)
print("Document updated: " + str(result.modified_count))

# print updated document
pprint.pprint(provinsi_collection.find_one(document_to_update))

# close the client
client.close()