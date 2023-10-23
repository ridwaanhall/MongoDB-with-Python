import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)


# ====================================================
# Dapatkan referensi ke basis data 'pendataan_penduduk'
db = client.pendataan_penduduk

# ====================================================
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


# ==================================================
# Dapatkan referensi ke koleksi 'KabupatenKota'
kabupaten_kota_collection = db["KabupatenKota"]

kabupaten_kota_data = [
    {"id_kabupaten_kota": 101, "nama_kabupaten_kota": "Bandung", "id_provinsi": 1},
    {"id_kabupaten_kota": 102, "nama_kabupaten_kota": "Surabaya", "id_provinsi": 2},
    {"id_kabupaten_kota": 103, "nama_kabupaten_kota": "Semarang", "id_provinsi": 3},
    {"id_kabupaten_kota": 201, "nama_kabupaten_kota": "Padang", "id_provinsi": 4},
    {"id_kabupaten_kota": 202, "nama_kabupaten_kota": "Palembang", "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data Kabupaten/Kota ke koleksi 'KabupatenKota'
result = kabupaten_kota_collection.insert_many(kabupaten_kota_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ========================================
# Dapatkan referensi ke koleksi 'Kecamatan'
kecamatan_collection = db["Kecamatan"]

kecamatan_data = [
    {"id_kecamatan": 1001, "nama_kecamatan": "Cimahi", "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"id_kecamatan": 1002, "nama_kecamatan": "Sidoarjo", "id_kabupaten_kota": 102, "id_provinsi": 2},
    {"id_kecamatan": 1003, "nama_kecamatan": "Salatiga", "id_kabupaten_kota": 103, "id_provinsi": 3},
    {"id_kecamatan": 2001, "nama_kecamatan": "Padang Barat", "id_kabupaten_kota": 201, "id_provinsi": 4},
    {"id_kecamatan": 2002, "nama_kecamatan": "Padang Selatan", "id_kabupaten_kota": 202, "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data Kecamatan ke koleksi 'Kecamatan'
result = kecamatan_collection.insert_many(kecamatan_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ================================================
# Dapatkan referensi ke koleksi 'Desa'
desa_collection = db["Desa"]

desa_data = [
    {"id_desa": 10001, "nama_desa": "Cisitu", "id_kecamatan": 1001, "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"id_desa": 10002, "nama_desa": "Waru", "id_kecamatan": 1002, "id_kabupaten_kota": 102, "id_provinsi": 2},
    {"id_desa": 10003, "nama_desa": "Sidorejo", "id_kecamatan": 1003, "id_kabupaten_kota": 103, "id_provinsi": 3},
    {"id_desa": 20001, "nama_desa": "Bungus", "id_kecamatan": 2001, "id_kabupaten_kota": 201, "id_provinsi": 4},
    {"id_desa": 20002, "nama_desa": "Caringin", "id_kecamatan": 2002, "id_kabupaten_kota": 202, "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data Desa ke koleksi 'Desa'
result = desa_collection.insert_many(desa_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'Dukuh'
dukuh_collection = db["Dukuh"]

dukuh_data = [
    {"id_dukuh": 100001, "nama_dukuh": "Dukuh 1", "id_desa": 10001, "id_kecamatan": 1001, "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"id_dukuh": 100002, "nama_dukuh": "Dukuh 2", "id_desa": 10002, "id_kecamatan": 1002, "id_kabupaten_kota": 102, "id_provinsi": 2},
    {"id_dukuh": 100003, "nama_dukuh": "Dukuh 3", "id_desa": 10003, "id_kecamatan": 1003, "id_kabupaten_kota": 103, "id_provinsi": 3},
    {"id_dukuh": 200001, "nama_dukuh": "Bungus 1", "id_desa": 20001, "id_kecamatan": 2001, "id_kabupaten_kota": 201, "id_provinsi": 4},
    {"id_dukuh": 200002, "nama_dukuh": "Bungus 2", "id_desa": 20002, "id_kecamatan": 2002, "id_kabupaten_kota": 202, "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data Dukuh ke koleksi 'Dukuh'
result = dukuh_collection.insert_many(dukuh_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'RW'
rw_collection = db["RW"]

rw_data = [
    {"no_rw": 1, "id_dukuh": 100001, "id_desa": 10001, "id_kecamatan": 1001, "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"no_rw": 2, "id_dukuh": 100002, "id_desa": 10002, "id_kecamatan": 1002, "id_kabupaten_kota": 102, "id_provinsi": 2},
    {"no_rw": 3, "id_dukuh": 100003, "id_desa": 10003, "id_kecamatan": 1003, "id_kabupaten_kota": 103, "id_provinsi": 3},
    {"no_rw": 101, "id_dukuh": 200001, "id_desa": 20001, "id_kecamatan": 2001, "id_kabupaten_kota": 201, "id_provinsi": 4},
    {"no_rw": 102, "id_dukuh": 200002, "id_desa": 20002, "id_kecamatan": 2002, "id_kabupaten_kota": 202, "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data RW ke koleksi 'RW'
result = rw_collection.insert_many(rw_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================


# ==============================================


# ==============================================


# ==============================================


# ==============================================


# ==============================================


# ==============================================


# ==============================================


client.close()
