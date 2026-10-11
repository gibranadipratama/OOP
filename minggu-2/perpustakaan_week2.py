# Tugas Praktikum 1

# class Buku
class Buku:
    # atribut class
    jumlah_buku_terdaftar = 0
    
    # constructor
    def __init__(self, judul, penulis, stok):
        self.judul = judul                      # atribut instance
        self.penulis = penulis                  # atribut instance
        self.stok = stok                        # atribut instance
        Buku.jumlah_buku_terdaftar += 1

    # Method tampilkan_info()
    def tampilkan_info(self):
        print(f"Judul : {self.judul}")
        print(f"Penulis : {self.penulis}")
        print(f"Stok : {self.stok}")
        


# object dari class Buku
buku1 = Buku("Belajar Python", "Budi Raharjo", 5)
buku2 = Buku("Struktur Data", "Siti Amina", 3)
buku3 = Buku("Basis Data", "Andi Wijaya", 7)

buku1.tampilkan_info()
buku2.tampilkan_info()
buku3.tampilkan_info()
print(f"Total buku terdaftar: {Buku.jumlah_buku_terdaftar}")


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
        print(f"Nama : {self.nama}")
        print(f"No. Anggota : {self.nomor_anggota}")
        print(f"Buku Dipinjam : {self.buku_dipinjam}")

# Object Anggota
anggota1 = Anggota("Dian Pratama", "A001")
anggota1.pinjam_buku("Belajar Python")
anggota1.pinjam_buku("Struktur Data")
anggota1.tampilkan_anggota()