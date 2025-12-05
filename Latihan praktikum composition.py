# Class Penulis dengan atribut nama.
class Penulis:
    """Kelas untuk merepresentasikan Penulis."""
    def __init__(self, nama):
        self.nama = nama
        
    def get_nama(self):
        return self.nama

# Class Buku yang memiliki Penulis (composition).
class Buku:
    """Kelas untuk merepresentasikan Buku.
    Memiliki objek Penulis (komposisi)."""
    
    def __init__(self, judul, penulis_obj):
        self.judul = judul
        # Komposisi: Objek Penulis adalah bagian dari objek Buku
        self.penulis = penulis_obj 
        
    def info_buku(self):
        # Mengakses nama penulis melalui objek penulis yang terkomposisi
        nama_penulis = self.penulis.get_nama()
        return f"Buku: '{self.judul}' oleh {nama_penulis}"

# Demonstrasikan cara mengakses data penulis dari objek buku.
# Instansiasi objek Penulis
penulis_satu = Penulis("Andrea Hirata")

# Instansiasi objek Buku, dengan memasukkan objek penulis ke dalamnya
buku_satu = Buku("Laskar Pelangi", penulis_satu)

# Mengakses dan mencetak informasi buku
print(buku_satu.info_buku())

# Demonstrasi langsung mengakses data penulis dari objek buku
print(f"Judul buku: {buku_satu.judul}")
print(f"Nama penulis (diakses via buku): {buku_satu.penulis.get_nama()}")
# Atau secara langsung:
print(f"Nama penulis (diakses via atribut nama): {buku_satu.penulis.nama}")