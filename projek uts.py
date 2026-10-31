import sys
import time

# =====================================================================
# BAGIAN 1: ENTITAS DATA & SISTEM UTAMA (STRUKTUR DATA TERPILIH)
# =====================================================================

class Produk:
    """Class Blueprint untuk objek Produk (Enkapsulasi OOP)."""
    def __init__(self, id_produk: str, nama: str, kategori: str, harga: float, stok: int):
        self.id_produk = id_produk
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"[{self.id_produk}] {self.nama} | Kat: {self.kategori} | Rp{self.harga:,.0f} | Stok: {self.stok}"


class SistemInventaris:
    """Class Pengelola Inventaris menggunakan Hash Table (Python dict).
       Kompleksitas Waktu: O(1) untuk Insert, Search, dan Delete.
    """
    def __init__(self):
        # Struktur Data Utama: Dictionary sebagai Hash Table
        self._data = {}

    def tambah_produk(self, produk: Produk) -> bool:
        # Cek keunikan ID dalam O(1)
        if produk.id_produk in self._data:
            return False 
        # Insert dalam O(1)
        self._data[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk: str) -> Produk | None:
        # Pencarian instan by Key dalam O(1)
        return self._data.get(id_produk, None)

    def hapus_produk(self, id_produk: str) -> bool:
        # Penghapusan by Key dalam O(1)
        if id_produk in self._data:
            del self._data[id_produk]
            return True
        return False

    def tampilkan_semua(self):
        if not self._data:
            print("\n[!] Data inventaris kosong.")
            return
        
        print("\n" + "="*70)
        print(f"{'ID PRODUK':<10} | {'NAMA PRODUK':<20} | {'HARGA':<12} | {'STOK':<5}")
        print("="*70)
        for p in self._data.values():
            print(f"{p.id_produk:<10} | {p.nama:<20} | Rp{p.harga:<9,.0f} | {p.stok:<5}")
        print("="*70)


# =====================================================================
# BAGIAN 2: STRUKTUR DATA PEMBANDING (UNTUK UJI KOMPLEKSITAS)
# =====================================================================

class Node:
    """Node untuk Linked List."""
    def __init__(self, id_produk: str, nama: str):
        self.id_produk = id_produk
        self.nama = nama
        self.next = None

class LinkedListADT:
    """Custom Linked List - Kompleksitas O(n)."""
    def __init__(self):
        self.head = None

    def insert(self, id_p: str, nama: str):
        new_node = Node(id_p, nama)
        new_node.next = self.head
        self.head = new_node

    def search(self, id_p: str):
        curr = self.head
        while curr:
            if curr.id_produk == id_p:
                return curr
            curr = curr.next
        return None

    def delete(self, id_p: str) -> bool:
        curr = self.head
        prev = None
        while curr:
            if curr.id_produk == id_p:
                if prev: prev.next = curr.next
                else: self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

class ArrayListADT:
    """Array List (Python list) - Kompleksitas O(n)."""
    def __init__(self):
        self.data = []

    def insert(self, id_p: str, nama: str):
        self.data.append((id_p, nama))

    def search(self, id_p: str):
        for item in self.data:
            if item[0] == id_p:
                return item
        return None

    def delete(self, id_p: str) -> bool:
        for i, item in enumerate(self.data):
            if item[0] == id_p:
                self.data.pop(i)
                return True
        return False


# =====================================================================
# BAGIAN 3: MODUL BENCHMARK (PENGHASIL DATA UNTUK LAPORAN TABEL)
# =====================================================================

def jalankan_benchmark():
    JUMLAH_DATA = 50_000
    TARGET_ID_LIST = f"PRD_{JUMLAH_DATA - 1}" # Worst case Array (Paling Akhir)
    TARGET_ID_LINKED = "PRD_0"                # Worst case Linked List (Paling Akhir karena insert di head)
    
    print(f"\n[!] Mempersiapkan uji performa pada {JUMLAH_DATA:,} data...")
    ds_hash = SistemInventaris()
    ds_list = ArrayListADT()
    ds_linked = LinkedListADT()

    # 1. Uji Penyisipan (Insert)
    print("\n--- A. UJI PENYISIPAN (INSERT) ---")
    
    t0 = time.perf_counter()
    for i in range(JUMLAH_DATA): ds_hash.tambah_produk(Produk(f"PRD_{i}", f"Barang_{i}", "Test", 1000, 10))
    t_hash_in = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    for i in range(JUMLAH_DATA): ds_list.insert(f"PRD_{i}", f"Barang_{i}")
    t_list_in = time.perf_counter() - t0

    t0 = time.perf_counter()
    for i in range(JUMLAH_DATA): ds_linked.insert(f"PRD_{i}", f"Barang_{i}")
    t_linked_in = time.perf_counter() - t0

    print(f"1. Hash Table   : {t_hash_in:.4f} detik [O(1)]")
    print(f"2. Array List   : {t_list_in:.4f} detik [O(1) amortized]")
    print(f"3. Linked List  : {t_linked_in:.4f} detik [O(1) di head]")

    # 2. Uji Pencarian (Search by ID)
    print("\n--- B. UJI PENCARIAN (SEARCH BY ID WORST CASE) ---")
    
    t0 = time.perf_counter()
    ds_hash.cari_produk(TARGET_ID_LIST)
    print(f"1. Hash Table   : {(time.perf_counter() - t0):.8f} detik [O(1)]")

    t0 = time.perf_counter()
    ds_list.search(TARGET_ID_LIST)
    print(f"2. Array List   : {(time.perf_counter() - t0):.8f} detik [O(n)]")

    t0 = time.perf_counter()
    ds_linked.search(TARGET_ID_LINKED)
    print(f"3. Linked List  : {(time.perf_counter() - t0):.8f} detik [O(n)]")

    # 3. Uji Penghapusan (Delete by ID)
    print("\n--- C. UJI PENGHAPUSAN (DELETE BY ID WORST CASE) ---")
    
    t0 = time.perf_counter()
    ds_hash.hapus_produk(TARGET_ID_LIST)
    print(f"1. Hash Table   : {(time.perf_counter() - t0):.8f} detik [O(1)]")

    t0 = time.perf_counter()
    ds_list.delete(TARGET_ID_LIST)
    print(f"2. Array List   : {(time.perf_counter() - t0):.8f} detik [O(n)]")

    t0 = time.perf_counter()
    ds_linked.delete(TARGET_ID_LINKED)
    print(f"3. Linked List  : {(time.perf_counter() - t0):.8f} detik [O(n)]")


# =====================================================================
# BAGIAN 4: MENU COMMAND LINE INTERFACE (CLI)
# =====================================================================

def main():
    sistem = SistemInventaris()
    
    # Masukkan beberapa data awal agar program tidak kosong saat presentasi
    sistem.tambah_produk(Produk("P001", "Laptop ASUS", "Komputer", 12000000, 5))
    sistem.tambah_produk(Produk("P002", "Mouse Logitech", "Aksesoris", 250000, 15))

    while True:
        print("\n" + "="*45)
        print(" SISTEM MANAJEMEN INVENTARIS E-COMMERCE")
        print("="*45)
        print("1. Daftarkan Produk Baru")
        print("2. Cari Detail Produk (berdasarkan ID)")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("5. [Lab] Uji Kecepatan Algoritma (Benchmark)")
        print("6. Keluar Program")
        
        pilihan = input("Pilih Menu (1-6): ").strip()

        if pilihan == "1":
            print("\n-- PENDAFTARAN PRODUK BARU --")
            id_p = input("ID Produk     : ").strip()
            nama = input("Nama Produk   : ").strip()
            kat  = input("Kategori      : ").strip()
            try:
                harga = float(input("Harga (Rp)    : "))
                stok  = int(input("Jumlah Stok   : "))
                if sistem.tambah_produk(Produk(id_p, nama, kat, harga, stok)):
                    print("[✓] Sukses: Produk berhasil disimpan ke Hash Table.")
                else:
                    print("[!] Gagal: ID Produk sudah terdaftar!")
            except ValueError:
                print("[!] Error: Harga dan Stok wajib diisi dengan angka.")

        elif pilihan == "2":
            print("\n-- PENCARIAN PRODUK --")
            id_p = input("Masukkan ID Produk: ").strip()
            hasil = sistem.cari_produk(id_p)
            if hasil:
                print(f"[✓] Produk Ditemukan:\n{hasil}")
            else:
                print(f"[!] Produk dengan ID '{id_p}' tidak ditemukan.")

        elif pilihan == "3":
            print("\n-- PENGHAPUSAN PRODUK --")
            id_p = input("Masukkan ID Produk yang ingin dihapus: ").strip()
            if sistem.hapus_produk(id_p):
                print(f"[✓] Sukses: Produk '{id_p}' berhasil dihapus.")
            else:
                print(f"[!] Gagal: Produk '{id_p}' tidak ditemukan.")

        elif pilihan == "4":
            sistem.tampilkan_semua()

        elif pilihan == "5":
            jalankan_benchmark()

        elif pilihan == "6":
            print("\nProgram dihentikan. Terima kasih!")
            sys.exit()
            
        else:
            print("[!] Menu tidak valid.")

if __name__ == "__main__":
    main()