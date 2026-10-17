class Burung:
    def __init__(self, nama, umur, jenis, warna_bulu, jenis_kelamin, makanan, bisa_terbang, habitat):
        # Atribut private (Enkapsulasi)
        self.__jenis = jenis
        self.__bisa_terbang = bisa_terbang

        # Atribut public
        self.nama = nama
        self.umur = umur
        self.warna_bulu = warna_bulu
        self.jenis_kelamin = jenis_kelamin
        self.makanan = makanan
        self.habitat = habitat

    # Getter untuk __jenis
    @property
    def jenis(self):
        return self.__jenis

    # Setter untuk __jenis dengan validasi
    @jenis.setter
    def jenis(self, jenis_burung):
        if isinstance(jenis_burung, str) and jenis_burung.strip() != "":
            self.__jenis = jenis_burung 
        else:
            raise ValueError("Input 'jenis' harus berupa string dan tidak boleh kosong!") 

    # Getter untuk __bisa_terbang
    @property
    def bisa_terbang(self):
        return self.__bisa_terbang

    # Setter untuk __bisa_terbang dengan validasi
    @bisa_terbang.setter
    def bisa_terbang(self, terbang):
        if isinstance(terbang, bool):
            self.__bisa_terbang = terbang
        else:
            raise ValueError("Input 'bisa_terbang' harus berupa boolean (True/False)!")

    # Method perilaku objek
    def terbang(self):
        if self.bisa_terbang:
            print(f"Burung bernama {self.nama} yang berjenis {self.jenis} mempunyai kemampuan untuk terbang tinggi.")
        else:
            print(f"Burung bernama {self.nama} yang berjenis {self.jenis} tidak mempunyai kemampuan untuk terbang.")

    def makan(self):
        print(f"{self.nama} sedang asyik memakan {self.makanan} di area {self.habitat}.")
    
    # Method untuk menampilkan data objek
    def cetak_info(self):
        print("--- Informasi Burung ---")
        print(f"Nama          : {self.nama}")
        print(f"Umur          : {self.umur} tahun")
        print(f"Jenis         : {self.jenis}")
        print(f"Warna Bulu    : {self.warna_bulu}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"Makanan       : {self.makanan}")
        status_terbang = "Ya" if self.bisa_terbang else "Tidak" 
        print(f"Bisa Terbang  : {status_terbang}")
        print(f"Habitat       : {self.habitat}")
        print("------------------------")


if __name__ == "__main__":
    # Instansiasi objek
    burung_merpati = Burung(
        nama="Supri",
        umur=1,
        jenis="Merpati", 
        warna_bulu="Coklat", 
        jenis_kelamin="Jantan", 
        makanan="Jagung", 
        bisa_terbang=True, 
        habitat="Pohon"
    )

    print("--- Menguji Method Awal ---")
    burung_merpati.cetak_info() 
    burung_merpati.terbang()
    burung_merpati.makan()

    print("\n--- Menguji Validasi Setter (Input Salah) ---")
    try:
        burung_merpati.jenis = 12345 
    except ValueError as e:
        print(f"Error tertangkap: {e}")

    try:
        burung_merpati.bisa_terbang = "Sangat Bisa" 
    except ValueError as e:
        print(f"Error tertangkap: {e}")

    print("\n--- Menguji Perubahan Setter (Input Benar) ---")
    print(f"Jenis sebelum diubah: {burung_merpati.jenis}")
    
    # Modifikasi state objek
    burung_merpati.jenis = "Burung Unta"
    burung_merpati.bisa_terbang = False
    burung_merpati.makanan = "Rumput"
    burung_merpati.habitat = "Padang Rumput"
    
    print(f"Jenis setelah diubah: {burung_merpati.jenis}")

    print("\n--- Menguji Method Setelah Modifikasi ---")
    burung_merpati.cetak_info() 
    burung_merpati.terbang()
    burung_merpati.makan()