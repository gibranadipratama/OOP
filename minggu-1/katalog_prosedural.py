katalog_buku = [
    {
        "Judul" : "Tutorial Python",
        "Penulis" : "alex",
        "Tahun" : "2025"
    },
    {
        "Judul" : "Tutorial OOP",
        "Penulis" : "Eko",
        "Tahun" : "2026"
    },
    {
        "Judul" : "Tutorial Jago Ngoding dalam 24jam",
        "Penulis" : "Sandhika",
        "Tahun" : "2024"
    }
]

for buku in katalog_buku:
    print("========================")
    for key, value in buku.items():
        print(f"- {key} : {value}")