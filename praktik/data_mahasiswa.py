def cari_mahasiswa(data, nim):
    return data.get(nim, "Data mahasiswa tidak ditemukan")


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# Pencarian mahasiswa
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "A003"))


# Penambahan mahasiswa
print("\n=== PENAMBAHAN MAHASISWA ===")
data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "C",
    "nilai": 90
}
print("Mahasiswa berhasil ditambahkan.")


# Pembaruan data mahasiswa
print("\n=== PEMBARUAN DATA MAHASISWA ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi:", data_mahasiswa["A002"]["nilai"])


# Rekap data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")
for nim, mahasiswa in data_mahasiswa.items():
    print(
        f"{nim} - {mahasiswa['nama']} - "
        f"Kelas {mahasiswa['kelas']} - "
        f"Nilai {mahasiswa['nilai']}"
    )


# Rata-rata nilai mahasiswa
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai: {rata_rata_nilai(data_mahasiswa):.2f}")