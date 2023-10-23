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
# Dapatkan referensi ke koleksi 'RT'
rt_collection = db["RT"]

rt_data = [
    {"no_rt": 101, "no_rw": 1, "id_dukuh": 100001, "id_desa": 10001, "id_kecamatan": 1001, "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"no_rt": 102, "no_rw": 1, "id_dukuh": 100001, "id_desa": 10001, "id_kecamatan": 1001, "id_kabupaten_kota": 101, "id_provinsi": 1},
    {"no_rt": 103, "no_rw": 2, "id_dukuh": 100002, "id_desa": 10002, "id_kecamatan": 1002, "id_kabupaten_kota": 102, "id_provinsi": 2},
    {"no_rt": 201, "no_rw": 3, "id_dukuh": 100003, "id_desa": 10003, "id_kecamatan": 1003, "id_kabupaten_kota": 103, "id_provinsi": 3},
    {"no_rt": 202, "no_rw": 101, "id_dukuh": 200001, "id_desa": 20001, "id_kecamatan": 2001, "id_kabupaten_kota": 201, "id_provinsi": 4},
    {"no_rt": 203, "no_rw": 102, "id_dukuh": 200002, "id_desa": 20002, "id_kecamatan": 2002, "id_kabupaten_kota": 202, "id_provinsi": 5}
]

# Tulis ekspresi yang memasukkan data RT ke koleksi 'RT'
result = rt_collection.insert_many(rt_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'Penduduk'
penduduk_collection = db["Penduduk"]

penduduk_data = [
    {"no_ktp": 12345, "nama_penduduk": "John Doe", "tempat_lahir": "Bandung", "tanggal_lahir": "1990-01-15", "pekerjaan": "PNS", "golongan_darah": "A+"},
    {"no_ktp": 67890, "nama_penduduk": "Jane Smith", "tempat_lahir": "Surabaya", "tanggal_lahir": "1985-05-20", "pekerjaan": "Dokter", "golongan_darah": "B-"},
    {"no_ktp": 11111, "nama_penduduk": "Alice Johnson", "tempat_lahir": "Salatiga", "tanggal_lahir": "2000-12-10", "pekerjaan": "Mahasiswa", "golongan_darah": "O+"},
    {"no_ktp": 22222, "nama_penduduk": "Bob Brown", "tempat_lahir": "Padang", "tanggal_lahir": "1988-07-25", "pekerjaan": "Guru", "golongan_darah": "AB+"},
    {"no_ktp": 33333, "nama_penduduk": "Eva White", "tempat_lahir": "Cimahi", "tanggal_lahir": "1995-03-30", "pekerjaan": "Wirausaha", "golongan_darah": "A-"},
    {"no_ktp": 44444, "nama_penduduk": "Frank Black", "tempat_lahir": "Sidoarjo", "tanggal_lahir": "1982-11-05", "pekerjaan": "Pengacara", "golongan_darah": "B+"},
    {"no_ktp": 55555, "nama_penduduk": "Grace Taylor", "tempat_lahir": "Semarang", "tanggal_lahir": "1979-09-12", "pekerjaan": "Dokter Gigi", "golongan_darah": "O-"}
]

# Tulis ekspresi yang memasukkan data Penduduk ke koleksi 'Penduduk'
result = penduduk_collection.insert_many(penduduk_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'Kelahiran'
kelahiran_collection = db["Kelahiran"]

kelahiran_data = [
    {"no_ktp": 12345, "nama_penduduk": "John Doe", "tempat_lahir": "Bandung", "tanggal_lahir": "1990-01-15"},
    {"no_ktp": 67890, "nama_penduduk": "Jane Smith", "tempat_lahir": "Surabaya", "tanggal_lahir": "1985-05-20"},
    {"no_ktp": 22222, "nama_penduduk": "Bob Brown", "tempat_lahir": "Padang", "tanggal_lahir": "1988-07-25"},
    {"no_ktp": 33333, "nama_penduduk": "Eva White", "tempat_lahir": "Cimahi", "tanggal_lahir": "1995-03-30"},
    {"no_ktp": 44444, "nama_penduduk": "Frank Black", "tempat_lahir": "Sidoarjo", "tanggal_lahir": "1982-11-05"},
    {"no_ktp": 55555, "nama_penduduk": "Grace Taylor", "tempat_lahir": "Semarang", "tanggal_lahir": "1979-09-12"}
]

# Tulis ekspresi yang memasukkan data Kelahiran ke koleksi 'Kelahiran'
result = kelahiran_collection.insert_many(kelahiran_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'Kematian'
kematian_collection = db["Kematian"]

kematian_data = [
    {"no_ktp": 11111, "nama_penduduk": "Alice Johnson", "tempat_kematian": "Salatiga", "tanggal_kematian": "2021-08-05", "sebab_kematian": "Sakit Parah"},
    {"no_ktp": 33333, "nama_penduduk": "Eva White", "tempat_kematian": "Cimahi", "tanggal_kematian": "2022-02-15", "sebab_kematian": "Kecelakaan"},
    {"no_ktp": 44444, "nama_penduduk": "Frank Black", "tempat_kematian": "Sidoarjo", "tanggal_kematian": "2020-11-10", "sebab_kematian": "Kanker"},
    {"no_ktp": 55555, "nama_penduduk": "Grace Taylor", "tempat_kematian": "Semarang", "tanggal_kematian": "2021-06-20", "sebab_kematian": "Kematian"},
    {"no_ktp": 22222, "nama_penduduk": "Bob Brown", "tempat_kematian": "Padang", "tanggal_kematian": "2021-08-05", "sebab_kematian": "Kecelakaan"},
    {"no_ktp": 67890, "nama_penduduk": "Jane Smith", "tempat_kematian": "Surabaya", "tanggal_kematian": "2022-02-15", "sebab_kematian": "Kecelakaan"}
]

# Tulis ekspresi yang memasukkan data Kematian ke koleksi 'Kematian'
result = kematian_collection.insert_many(kematian_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================
# Dapatkan referensi ke koleksi 'JenisKelamin'
jenis_kelamin_collection = db["JenisKelamin"]

jenis_kelamin_data = [
    {"no_ktp": 12345, "nama_ktp": "John Doe", "jenis_kelamin": "Pria"},
    {"no_ktp": 67890, "nama_ktp": "Jane Smith", "jenis_kelamin": "Wanita"},
    {"no_ktp": 11111, "nama_ktp": "Alice Johnson", "jenis_kelamin": "Wanita"},
    {"no_ktp": 22222, "nama_ktp": "Bob Brown", "jenis_kelamin": "Pria"},
    {"no_ktp": 33333, "nama_ktp": "Eva White", "jenis_kelamin": "Wanita"},
    {"no_ktp": 44444, "nama_ktp": "Frank Black", "jenis_kelamin": "Pria"},
    {"no_ktp": 55555, "nama_ktp": "Grace Taylor", "jenis_kelamin": "Wanita"}
]

# Tulis ekspresi yang memasukkan data JenisKelamin ke koleksi 'JenisKelamin'
result = jenis_kelamin_collection.insert_many(jenis_kelamin_data)

document_ids = result.inserted_ids
print("# of documents inserted: ", len(document_ids))
print(f"_ids of inserted documents: {document_ids}")


# ==============================================


# ==============================================


# ==============================================


client.close()
