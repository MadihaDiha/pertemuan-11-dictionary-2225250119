# Pertemuan 11 - Dictionary Python

## Identitas

- **Nama:** Madiha
- **NIM:** 2225250119
- **Kelas:** 3E
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Program Studi:** Pendidikan Matematika
- **Universitas:** Universitas Sultan Ageng Tirtayasa

## Tujuan

Mempelajari dictionary dalam Python, meliputi pembuatan dictionary, akses data menggunakan key, penggunaan metode `get()`, manipulasi data, iterasi dictionary, dictionary bersarang, serta penggunaan fungsi untuk mencari dan mengolah data mahasiswa agar program lebih terstruktur dan mudah dipahami.

## Struktur Folder

```text
pertemuan-11-dictionary-2225250119/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Materi yang Dipelajari

1. Membuat dictionary menggunakan pasangan key dan value.
2. Mengakses data dictionary menggunakan key.
3. Menggunakan metode `get()` untuk mengakses data dengan aman.
4. Memanipulasi dictionary dengan menambahkan, memperbarui, dan menghapus data.
5. Melakukan iterasi menggunakan metode `items()` untuk menampilkan key dan value.
6. Menggunakan dictionary bersarang (*nested dictionary*) untuk menyimpan data yang lebih terstruktur.
7. Membuat fungsi pencarian data mahasiswa berdasarkan NIM.
8. Menghitung rata-rata nilai mahasiswa menggunakan dictionary.
9. Melakukan pengujian program melalui terminal VS Code serta mengelola tugas menggunakan Git dan GitHub.

## Deskripsi Latihan

| File | Keterangan |
|---|---|
| `01_dasar_dictionary.py` | Membuat dictionary berisi NIM, nama, dan nilai, kemudian menampilkan data berdasarkan key. |
| `02_akses_get.py` | Mengakses data menggunakan metode `get()` serta menampilkan nilai default jika key tidak ditemukan. |
| `03_manipulasi_dictionary.py` | Menambahkan data kelas, memperbarui nilai, dan menghapus data menggunakan `pop()`. |
| `04_iterasi_dictionary.py` | Menampilkan seluruh key dan value menggunakan perulangan `for` dan metode `items()`. |
| `05_dictionary_bersarang.py` | Membuat nested dictionary untuk menyimpan data mahasiswa dan mengakses informasi di dalamnya. |
| `06_fungsi_dictionary.py` | Membuat fungsi pencarian mahasiswa berdasarkan NIM dan menampilkan pesan jika data tidak ditemukan. |
| `data_mahasiswa.py` | Mengelola data mahasiswa melalui operasi pencarian, penambahan, pembaruan, rekap data, dan perhitungan rata-rata nilai. |

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer dan terminal VS Code berada di folder utama proyek.

### 1. Menjalankan File Latihan

Jalankan setiap perintah berikut secara terpisah melalui terminal VS Code.

**Latihan 1 – Dasar Dictionary**
```bash
python latihan/01_dasar_dictionary.py
```

**Latihan 2 – Akses Data dengan `get()`**
```bash
python latihan/02_akses_get.py
```

**Latihan 3 – Manipulasi Dictionary**
```bash
python latihan/03_manipulasi_dictionary.py
```

**Latihan 4 – Iterasi Dictionary**
```bash
python latihan/04_iterasi_dictionary.py
```

**Latihan 5 – Dictionary Bersarang**
```bash
python latihan/05_dictionary_bersarang.py
```

**Latihan 6 – Fungsi Dictionary**
```bash
python latihan/06_fungsi_dictionary.py
```

### 2. Menjalankan Program Praktik

Jalankan perintah berikut untuk menjalankan program pengelolaan data mahasiswa.

```bash
python praktik/data_mahasiswa.py
```

## Hasil Pengujian Latihan

| No. | Program | Hasil Pengujian |
|---|---|---|
| 1 | Dasar dictionary | NIM = A001, nama = Ayu, nilai = 85. |
| 2 | Akses data dengan `get()` | Nama = Ayu, kelas = Belum ada. |
| 3 | Manipulasi dictionary | Data kelas berhasil ditambahkan dan dihapus, sedangkan nilai berubah dari 85 menjadi 90. |
| 4 | Iterasi dictionary | Menampilkan nama = Ayu, nilai = 85, dan kelas = A. |
| 5 | Dictionary bersarang | Nama mahasiswa A001 = Ayu dan nilai mahasiswa A002 = 78. |
| 6 | Fungsi dictionary | Data A002 menampilkan Budi dengan nilai 78, sedangkan A003 menampilkan pesan data tidak ditemukan. |

## Hasil Pengujian Praktik

Program praktik `data_mahasiswa.py` menggunakan dictionary untuk menyimpan dan mengelola data mahasiswa.

### Data Mahasiswa Awal

| NIM | Nama | Kelas | Nilai Awal |
|---|---|---|---:|
| A001 | Ayu | A | 85 |
| A002 | Budi | A | 78 |
| A003 | Citra | B | 92 |
| A004 | Deni | B | 74 |
| A005 | Eka | A | 88 |

### Hasil Pengujian Operasi

| Operasi | Input | Hasil Pengujian |
|---|---|---|
| Pencarian mahasiswa | NIM = A003 | Citra ditemukan, kelas B, nilai 92. |
| Penambahan mahasiswa | NIM = A006 | Fani berhasil ditambahkan dengan kelas C dan nilai 90. |
| Pembaruan nilai | NIM = A002 | Nilai Budi berubah dari 78 menjadi 82. |
| Rekap data mahasiswa | Seluruh data mahasiswa | Berhasil menampilkan 6 mahasiswa. |
| Menghitung rata-rata | 6 mahasiswa setelah pembaruan | Rata-rata nilai sebesar 85,17. |

Berdasarkan hasil pengujian, program berhasil melakukan seluruh operasi pengelolaan data mahasiswa. Data baru dapat ditambahkan, nilai mahasiswa dapat diperbarui, dan seluruh data dapat ditampilkan melalui iterasi dictionary. Rata-rata nilai mahasiswa setelah penambahan dan pembaruan data adalah **85,17**.

## Kuis Formatif - Pertemuan 11

| No. | Pertanyaan | Jawaban |
|---|---|---|
| 1 | Apa perbedaan utama list dan dictionary? | List menyimpan data berdasarkan indeks, sedangkan dictionary menyimpan data dalam pasangan key dan value. |
| 2 | Apa fungsi key dalam dictionary? | Key berfungsi sebagai kunci untuk mengidentifikasi dan mengakses value tertentu dalam dictionary. |
| 3 | Apa yang terjadi jika `data['kelas']` dipanggil saat key `'kelas'` tidak ada? | Python menghasilkan `KeyError` karena key tersebut tidak ditemukan. |
| 4 | Apa perbedaan `data['kelas']` dengan `data.get('kelas')`? | `data['kelas']` menghasilkan `KeyError` jika key tidak ada, sedangkan `data.get('kelas')` mengembalikan `None` secara default. |
| 5 | Bagaimana memeriksa apakah suatu key tersedia? | Menggunakan operator `in`, misalnya `'kelas' in data`. |
| 6 | Apa fungsi `items()`? | Mengambil pasangan key dan value dalam dictionary sehingga dapat digunakan dalam perulangan. |
| 7 | Bagaimana menambahkan pasangan key-value baru? | Menetapkan key dan value baru, misalnya `data['kelas'] = 'A'`. |
| 8 | Bagaimana mengubah value dari key yang sudah ada? | Menetapkan value baru pada key tersebut, misalnya `data['nilai'] = 90`. |
| 9 | Dalam data pendidikan, mengapa NIM cocok digunakan sebagai key? | Karena NIM merupakan identitas unik mahasiswa yang memudahkan pencarian dan pengelolaan data. |
| 10 | Perintah apa yang digunakan untuk mengirim commit ke GitHub? | Menggunakan `git push origin main` untuk mengirim commit dari branch `main` ke GitHub. |

## Refleksi

Melalui pertemuan ini, saya mempelajari cara menyimpan dan mengelola data menggunakan dictionary dalam Python. Saya memahami bahwa dictionary menyimpan data dalam bentuk pasangan key dan value sehingga informasi dapat diakses berdasarkan key yang sesuai.

Saya juga mempelajari penggunaan metode `get()` untuk mengakses data dengan aman, manipulasi dictionary untuk menambahkan, memperbarui, dan menghapus data, serta iterasi untuk menampilkan seluruh isi dictionary. Selain itu, penggunaan dictionary bersarang membantu saya memahami cara menyimpan data mahasiswa dengan beberapa informasi dalam satu struktur data.

Pada kegiatan praktik, saya menerapkan dictionary untuk melakukan pencarian, penambahan, pembaruan, rekap data mahasiswa, dan perhitungan rata-rata nilai. Program telah dijalankan melalui terminal VS Code dan menghasilkan keluaran sesuai dengan yang diharapkan. Materi ini membantu saya meningkatkan pemahaman mengenai struktur data dan pengolahan data menggunakan Python.
