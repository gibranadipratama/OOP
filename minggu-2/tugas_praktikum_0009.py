# Tugas Praktikum 1 - Sistem Perpustakaan Sederhana

# class Buku
class Buku:
    # atribut class
    jumlah_buku_terdaftar = 0

    # constructor
    def __init__(self, judul, penulis, stok):
        self.judul = judul          # atribut instance
        self.penulis = penulis      # atribut instance
        self.stok = stok            # atribut instance
        # setiap object baru dihitung saat dibuat
        Buku.jumlah_buku_terdaftar += 1

    # Method tampilkan_info()
    def tampilkan_info(self):
        print(f"Judul   : {self.judul}")
        print(f"Penulis : {self.penulis}")
        print(f"Stok    : {self.stok}")

    # Method tambah_stok()
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penambahan harus lebih dari 0.")
            return
        self.stok += jumlah
        print(f"Stok '{self.judul}' bertambah {jumlah}. Stok sekarang: {self.stok}")

    # Method kurangi_stok()
    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah pengurangan harus lebih dari 0.")
            return
        if jumlah > self.stok:
            print(f"Gagal: stok '{self.judul}' hanya {self.stok}, "
                  f"tidak bisa dikurangi {jumlah}.")
            return
        self.stok -= jumlah
        print(f"Stok '{self.judul}' berkurang {jumlah}. Stok sekarang: {self.stok}")


# class Anggota
class Anggota:
    # constructor
    def __init__(self, nama, nomor_anggota):
        self.nama = nama
        self.nomor_anggota = nomor_anggota
        self.buku_dipinjam = []

    # Method pinjam_buku()
    def pinjam_buku(self, judul_buku):
        self.buku_dipinjam.append(judul_buku)
        print(f"{self.nama} meminjam '{judul_buku}'")

    # Method tampilkan_anggota()
    def tampilkan_anggota(self):
        print(f"Nama          : {self.nama}")
        print(f"No. Anggota   : {self.nomor_anggota}")
        print(f"Buku Dipinjam : {self.buku_dipinjam}")

    # Method kembalikan_buku()
    def kembalikan_buku(self, buku):
        if buku.judul not in self.buku_dipinjam:
            print(f"Gagal: {self.nama} tidak sedang meminjam '{buku.judul}'.")
            return
        self.buku_dipinjam.remove(buku.judul)
        print(f"{self.nama} mengembalikan '{buku.judul}'")
        buku.tambah_stok(1)

# ---------- Object Buku ----------
buku1 = Buku("Algoritma dan Logika", "Seno Parulian", 4)
buku2 = Buku("Jaringan Komputer Dasar", "Jin Faraday", 2)
buku3 = Buku("Pemrograman Web", "Joni Sutanto", 6)

# ---------- Object Anggota ----------
anggota1 = Anggota("Gibran Adi Pratama", "A101")
anggota2 = Anggota("Dante Vicente", "A102")

# ---------- Uji method tambah_stok & kurangi_stok ----------
print("=== Uji Stok ===")
buku3.tambah_stok(4)        # stok 6 -> 10
buku2.kurangi_stok(5)       # gagal, stok hanya 2 (tidak boleh negatif)
buku2.kurangi_stok(1)       # berhasil, stok 2 -> 1
buku2.tambah_stok(2)        # kembali ke 3

# ---------- Simulasi peminjaman ----------
# Gibran meminjam dua buku yang berbeda
print("\n=== Proses Peminjaman ===")
anggota1.pinjam_buku(buku1.judul)
buku1.kurangi_stok(1)
anggota1.pinjam_buku(buku3.judul)
buku3.kurangi_stok(1)

# ---------- Simulasi pengembalian ----------
print("\n=== Proses Pengembalian ===")
anggota1.kembalikan_buku(buku1)     # berhasil, stok buku1 3 -> 4
anggota2.kembalikan_buku(buku2)     # gagal, anggota2 tidak meminjam buku2

# ---------- Informasi akhir ----------
print("\n=== Info Akhir Buku ===")
for buku in (buku1, buku2, buku3):
    buku.tampilkan_info()
    print()

print("=== Info Anggota yang Meminjam ===")
anggota1.tampilkan_anggota()

print(f"\nTotal buku terdaftar: {Buku.jumlah_buku_terdaftar}")