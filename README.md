# Sistem Manajemen Inventaris E-Commerce

Proyek ini adalah implementasi Sistem Manajemen Inventaris Produk E-Commerce berskala besar yang dikembangkan menggunakan Python berbasis Object-Oriented Programming (OOP). Proyek ini ditujukan untuk memenuhi tugas evaluasi (UTS) Analisis Struktur Data dan Algoritma.

## Skenario Kasus
Sistem dirancang untuk menangani jutaan data produk yang dinamis. Operasi utama yang membutuhkan efisiensi waktu pengeksekusian tinggi meliputi:
1. Pendaftaran produk baru (dengan validasi ID unik).
2. Pencarian detail produk berdasarkan ID.
3. Penghapusan produk dari peredaran.

## Analisis Struktur Data & Kompleksitas Waktu (Big-O)
Berdasarkan hasil pengujian komparatif, sistem ini menggunakan **Hash Table (`Python dict`)** sebagai struktur data utama, mengungguli *Array List* dan *Linked List*.

| Struktur Data | Insert (Unique) | Search by ID | Delete by ID |
| :--- | :---: | :---: | :---: |
| **Hash Table** (Utama) | **O(1)** | **O(1)** | **O(1)** |
| **Array List** (Pembanding) | O(n) | O(n) | O(n) |
| **Linked List** (Pembanding)| O(n) | O(n) | O(n) |

**Justifikasi:**
Hash Table dipilih karena mampu melakukan pemetaan kunci (ID Produk) secara langsung ke alamat memori. Hal ini memungkinkan operasi *Insert*, *Search*, dan *Delete* berjalan dalam waktu konstan $O(1)$, menghindari *bottleneck* pencarian linear dan beban *memory shifting* $O(n)$ yang terjadi pada List dan Linked List.

## Fitur Program (CLI)
1. **Daftarkan Produk Baru**: Menambahkan objek `Produk` ke dalam Hash Table.
2. **Cari Detail Produk**: Menampilkan spesifikasi produk dalam waktu $O(1)$.
3. **Hapus Produk**: Menghapus data dari memori secara instan.
4. **Tampilkan Semua Produk**: Melakukan *traversal* seluruh isi inventaris.
5. **Uji Kecepatan Algoritma (Benchmark)**: Fitur eksperimental untuk menguji dan membandingkan performa Hash Table, Array List, dan Linked List secara *real-time* menggunakan modul `time.perf_counter()` pada 50.000 sampel data.

## Cara Menjalankan Program
Pastikan Python 3.x sudah terinstal, lalu jalankan perintah berikut di terminal:

```bash
python main_inventaris.py