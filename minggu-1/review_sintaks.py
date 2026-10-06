# 1. Variable dan tipe data
nama = "Perpustakaan Digital" # tipe data String
jumlah_anggota = 120          # tipe data Integer
rata_rata_kunjungan = 35.5    # tipe data float

# 2. Struktur kontrol (if-else)
if jumlah_anggota > 100:
    print("Perpustakaan besar")
else:
    print("Perpustakaan kecil")

# 3. perulangan (looping)
daftar_buku = ["Belajar Python", "Struktur Data", "Basis Data"]
for buku in daftar_buku:
    print(f"- {buku}")

# 4. function
def sapa(nama_anggota):
    return f"Selamat datang, {nama_anggota}"

print(sapa("Dian"))