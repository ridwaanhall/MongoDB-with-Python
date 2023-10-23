import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# Dapatkan referensi ke basis data 'pendataan_penduduk'
db = client.pendataan_penduduk

# Dapatkan referensi ke koleksi 'Provinsi'
provinsi_collection = db["Provinsi"]

provinsi_data = [
    {"id_provinsi": 1, "nama_provinsi": "Jawa Barat"},
    {"id_provinsi": 2, "nama_provinsi": "Jawa Timur"},
    {"id_provinsi": 3, "nama_provinsi": "Jawa Tengah"},
    {"id_provinsi": 4, "nama_provinsi": "Sumatera Barat"},
    {"id_provinsi": 5, "nama_provinsi": "Sumatera Utara"}
]

# Tulis ekspresi yang memasukkan data provinsi ke koleksi 'Provinsi'
result = provinsi_collection.insert_many(provinsi_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")

client.close()
