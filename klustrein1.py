# DATA HASIL KUESIONER

# Skala Likert:
# 1 = Sangat Mudah
# 2 = Mudah
# 3 = Cukup Sulit
# 4 = Sulit
# 5 = Sangat Sulit

# nilai[0] = Penggunaan Syntax
# nilai[1] = Pemahaman Logika
# nilai[2] = Debugging

data_kuesioner = [
    {"nama": "Zahra", "nilai": [4,4,4]},
    {"nama": "Lionel", "nilai": [4,4,5]},
    {"nama": "Nazhwa", "nilai": [3,3,2]},
    {"nama": "Belva", "nilai": [1,2,2]},
    {"nama": "Indah", "nilai": [3,2,2]},
    {"nama": "Dzakwan", "nilai": [5,3,3]},
    {"nama": "Isnaeni", "nilai": [4,3,2]},
    {"nama": "Sigit", "nilai": [4,4,4]},
    {"nama": "Rifdha", "nilai": [3,4,4]},
    {"nama": "Zahid", "nilai": [4,4,3]},
    {"nama": "Adiba", "nilai": [4,2,1]},
    {"nama": "Khansa", "nilai": [4,5,5]},
    {"nama": "Sylvia", "nilai": [4,3,4]},
    {"nama": "Muhamad Zaldi", "nilai": [4,4,2]},
    {"nama": "Kayla", "nilai": [3,4,3]},
    {"nama": "Aisya", "nilai": [2,2,1]},
    {"nama": "Ara", "nilai": [5,5,5]},
    {"nama": "Daffa Fauzan", "nilai": [1,1,1]},
    {"nama": "Ridwan", "nilai": [5,4,3]},
    {"nama": "Najib", "nilai": [3,3,3]},
    {"nama": "Yahfasyat", "nilai": [4,4,5]},
    {"nama": "Daffa Safaraz", "nilai": [3,4,5]},
    {"nama": "Zidni", "nilai": [4,4,4]},
    {"nama": "Faiz M", "nilai": [3,2,4]},
    {"nama": "Keysha Ega", "nilai": [4,2,5]},
    {"nama": "Afif Fajar", "nilai": [4,3,4]},
    {"nama": "Luthfi", "nilai": [5,1,2]},
    {"nama": "Daffa Ziyad", "nilai": [2,3,3]},
    {"nama": "Lucky", "nilai": [4,4,2]}
]

# MENGHITUNG RATA-RATA HASIL KUESIONER

jumlah_responden = len(data_kuesioner)

total_syntax = 0
total_logika = 0
total_debugging = 0

for item in data_kuesioner:
    total_syntax += item["nilai"][0]
    total_logika += item["nilai"][1]
    total_debugging += item["nilai"][2]

rata_syntax = total_syntax / jumlah_responden
rata_logika = total_logika / jumlah_responden
rata_debugging = total_debugging / jumlah_responden

print("________________________________________")
print("       RATA-RATA HASIL KUESIONER")
print("________________________________________")

print(f"Rata-rata Penggunaan Syntax     = {rata_syntax:.2f}")
print(f"Rata-rata Pemahaman Logika      = {rata_logika:.2f}")
print(f"Rata-rata Debugging             = {rata_debugging:.2f}")

# VEKTOR DATA BAHASA C

vektor_c = [
    rata_syntax,
    rata_logika,
    rata_debugging
]

print("\nVektor Bahasa C:")
print(
    f"[{vektor_c[0]:.2f}, "
    f"{vektor_c[1]:.2f}, "
    f"{vektor_c[2]:.2f}]"
)

# PROSES K-MEANS CLUSTERING

# Jumlah cluster
K = 3

# Centroid awal (manual)
centroid = [
    [4,4,4], # Tingkat kesulitan tinggi
    [1,1,1], # Tingkat kesulitan rendah
    [5,5,5]  # Tingkat kesulitan sangat tinggi
]

# FUNGSI MENGHITUNG JARAK EUCLIDEAN


def hitung_jarak(data, centroid):
    jumlah = 0
    
    for i in range(len(data)):
        jumlah += (data[i] - centroid[i]) ** 2
    
    return jumlah ** 0.5

# MENAMPILKAN HASIL JARAK

print("\n________________________________________")
print("        HASIL PERHITUNGAN JARAK")
print("________________________________________")

for i in range(len(centroid)):
    jarak = hitung_jarak(vektor_c, centroid[i])
    
    print(
        f"Jarak ke Centroid {i+1} "
        f"{centroid[i]} = {jarak:.2f}"
    )

# MENENTUKAN CLUSTER TERDEKAT

jarak_terdekat = []
for i in range(len(centroid)):
    jarak = hitung_jarak(vektor_c, centroid[i])
    jarak_terdekat.append(jarak)

cluster = jarak_terdekat.index(min(jarak_terdekat)) + 1

