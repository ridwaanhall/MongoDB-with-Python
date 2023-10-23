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
document_to_delete = {"_id": ObjectId("65363ed53a0685c0ac931bad")}

# search for document before delete
print("searching for target document before delete: ")
pprint.pprint(provinsi_collection.find_one(document_to_delete))

# write an expression that deletes the target document.
result = provinsi_collection.delete_one(document_to_delete)

# search document after delete
print("searching for target document after delete: ")
pprint.pprint(provinsi_collection.find_one(document_to_delete))

print("DOcument deleted: " + str(result.deleted_count))

# close the client
client.close()