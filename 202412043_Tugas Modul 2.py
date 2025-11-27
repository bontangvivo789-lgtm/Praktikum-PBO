import datetime as dt
class Buku:
    def __init__(self, kode, judul, penulis, stok, lokasi):
        # Public Attributes
        self.kode_buku = kode
        self.judul = judul
        self.penulis = penulis
        
        # Protected Attribute (Stok)
        self._stok = stok
        
        # Private Attribute (Lokasi Rak)
        self.__lokasi_rak = lokasi

    # Getter/Setter Lokasi Rak (Private)
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    # Tambah/Kurangi Stok (Protected)
    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self._stok += jumlah
            return True
        return False

    def kurangi_stok(self, jumlah):
        if 0 < jumlah <= self._stok:
            self._stok -= jumlah
            return True
        return False
    
    def info_buku(self):
        """Menampilkan informasi buku."""
        return (f"[{self.kode_buku}] {self.judul} oleh {self.penulis} | "
                f"Stok: {self._stok} | Rak: {self.get_lokasi_rak()}")

class Peminjam:
    def __init__(self, kode_buku, tanggal_pinjam=None):
        # Atribut Public
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam if tanggal_pinjam else dt.date.today()
        
        # Atribut Public (akan diisi saat pengembalian)
        self.tanggal_kembali = None
        self.status = "Dipinjam" # Dipinjam / Dikembalikan

    def info_peminjaman(self):
        """Menampilkan informasi detail peminjaman."""
        tgl_kembali_str = str(self.tanggal_kembali) if self.tanggal_kembali else "-"
        return (f"Buku Kode: {self.kode_buku}, Tgl Pinjam: {self.tanggal_pinjam}, "
                f"Tgl Kembali: {tgl_kembali_str}, Status: {self.status}")

class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=2, status_aktif=True):
        # Public Attributes
        self.id_anggota = id_anggota
        self.nama = nama
        
        # Protected Attribute
        self._maks_pinjam = maks_pinjam
        
        # Private Attribute
        self.__status_aktif = status_aktif
        
        # Aggregation: Daftar Peminjaman (list objek Peminjam)
        self.daftar_peminjaman = []

    # Getter/Setter Status Aktif (Private)
    def get_status_aktif(self):
        return "Aktif" if self.__status_aktif else "Non-Aktif"

    def set_status_aktif(self, status: bool):
        self.__status_aktif = status
        
    def _jumlah_pinjaman_aktif(self):
        """Method helper (internal) untuk menghitung pinjaman yang masih 'Dipinjam'."""
        return sum(1 for p in self.daftar_peminjaman if p.status == "Dipinjam")

    def pinjam_buku(self, buku: Buku):
        """Memproses peminjaman buku."""
        if not self.__status_aktif:
            print(f"[{self.nama}] GAGAL pinjam: Status Anggota Tidak Aktif.")
            return False

        if self._jumlah_pinjaman_aktif() >= self._maks_pinjam:
            print(f"[{self.nama}] GAGAL pinjam: Sudah mencapai batas maksimal ({self._maks_pinjam} buku).")
            return False

        if buku.kurangi_stok(1): # Kurangi stok buku
            peminjaman_baru = Peminjam(buku.kode_buku)
            self.daftar_peminjaman.append(peminjaman_baru)
            print(f"[{self.nama}] BERHASIL meminjam '{buku.judul}'.")
            return True
        else:
            print(f"[{self.nama}] GAGAL pinjam: Stok buku '{buku.judul}' tidak mencukupi.")
            return False

    def kembalikan_buku(self, kode_buku, perpustakaan):
        """Memproses pengembalian buku."""
        for peminjaman in self.daftar_peminjaman:
            if peminjaman.kode_buku == kode_buku and peminjaman.status == "Dipinjam":
                # Update status peminjaman
                peminjaman.tanggal_kembali = dt.date.today()
                peminjaman.status = "Dikembalikan"
                
                # Tambah stok buku di perpustakaan
                buku = perpustakaan.cari_buku(kode_buku)
                if buku and buku.tambah_stok(1):
                    print(f"[{self.nama}] BERHASIL mengembalikan buku '{buku.judul}'.")
                    return True
                return False

        print(f"[{self.nama}] GAGAL mengembalikan: Buku kode {kode_buku} tidak ditemukan dalam pinjaman aktif.")
        return False
        
    def info_anggota(self):
        """Menampilkan informasi anggota."""
        return (f"[ID: {self.id_anggota}] Nama: {self.nama} | Status: {self.get_status_aktif()} | "
                f"Pinjaman Aktif: {self._jumlah_pinjaman_aktif()}")

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = {} # Composition: Buku tidak dapat berdiri tanpa Perpustakaan

    def tambah_buku(self, buku: Buku):
        """Menambahkan buku ke dalam koleksi (Composition)."""
        self.koleksi_buku[buku.kode_buku] = buku
        
    def cari_buku(self, kode_buku):
        """Mencari objek buku berdasarkan kode."""
        return self.koleksi_buku.get(kode_buku)
        
    def info_koleksi(self):
        """Menampilkan informasi semua buku."""
        print(f"\n--- Koleksi Buku {self.nama} ({len(self.koleksi_buku)} Judul) ---")
        for buku in self.koleksi_buku.values():
            print(f"  {buku.info_buku()}")
        print("-" * 45)

if __name__ == "__main__":
    # Inisiasi Perpustakaan
    lib = Perpustakaan("Perpustakaan Universitas X")

    # Buat 3 buku (Composition)
    b1 = Buku("B001", "Python Programming", "Guido van Rossum", 5, "A1")
    b2 = Buku("B002", "Data Structures", "Alfred Aho", 3, "A2")
    b3 = Buku("B003", "Machine Learning Intro", "Andrew Ng", 2, "B1")
    
    lib.tambah_buku(b1)
    lib.tambah_buku(b2)
    lib.tambah_buku(b3)

    # Buat 2 anggota (Aggregation: Anggota dapat ada tanpa Peminjaman)
    a1 = Anggota("A001", "Ani")
    a2 = Anggota("A002", "Budi")
    
    print("--- [1] KONDISI AWAL ---")
    lib.info_koleksi()
    print(f"Informasi Anggota 1: {a1.info_anggota()}")
    print(f"Informasi Anggota 2: {a2.info_anggota()}")

    # --- Peminjaman  ---
    print("\n--- [2] PROSES PEMINJAMAN ---")
    
    # Anggota 1 pinjam 2 buku
    a1.pinjam_buku(b1) # Pinjam B001
    a1.pinjam_buku(b2) # Pinjam B002
    
    # Coba pinjam buku ke-3 (Gagal karena maks pinjam = 2)
    a1.pinjam_buku(b3) 

    # Anggota 2 pinjam 1 buku
    a2.pinjam_buku(b3) # Pinjam B003
    
    # Coba pinjam B002 yang stoknya tinggal 2
    buku_pinjaman_sama = lib.cari_buku("B002")
    a2.pinjam_buku(buku_pinjaman_sama) # Pinjam B002

    # --- Demonstrasi ---
    print("\n--- [e.1 & e.2] INFORMASI BUKU DAN ANGGOTA SETELAH PINJAM ---")
    lib.info_koleksi() # Stok Buku berkurang
    print(f"Informasi Anggota 1: {a1.info_anggota()}")
    print(f"Informasi Anggota 2: {a2.info_anggota()}")

    # --- Pengembalian Buku ---
    print("\n--- [3] PROSES PENGEMBALIAN BUKU ---")
    
    # Anggota 1 kembalikan 1 buku
    a1.kembalikan_buku("B001", lib)
    
    # Coba kembalikan buku yang sudah dikembalikan (Gagal)
    a1.kembalikan_buku("B001", lib)

    # --- Demonstrasi (Langkah e) ---
    print("\n--- [e.3] DAFTAR PEMINJAMAN MASING-MASING ANGGOTA ---")
    
    print(f"\n[Anggota: {a1.nama}]")
    for p in a1.daftar_peminjaman:
        print(f"  -> {p.info_peminjaman()}")

    print(f"\n[Anggota: {a2.nama}]")
    for p in a2.daftar_peminjaman:
        print(f"  -> {p.info_peminjaman()}")
        
    print("\n--- [4] KONDISI AKHIR ---")
    lib.info_koleksi() # Stok Buku bertambah
    print(f"Informasi Anggota 1: {a1.info_anggota()}")
    print(f"Informasi Anggota 2: {a2.info_anggota()}")