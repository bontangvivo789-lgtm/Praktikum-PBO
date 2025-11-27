class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # Langkah f: Tambahkan method rata_rata()
    def rata_rata(self):
        """Menghitung rata-rata skor dari semua nilai yang dimiliki mahasiswa."""
        if not self.daftar_nilai:
            return 0.0
        total_skor = sum(n.skor for n in self.daftar_nilai)
        return total_skor / len(self.daftar_nilai)

class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)

class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# Fungsi report_program dari contoh sebelumnya
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print("\n" + "=" * 40)
    print(f"REPORT PROGRAM STUDI: {prodi.nama}")
    print("=" * 40)
    
    mk_kode_list = [mk.kode for mk in prodi.daftar_matakuliah]
    print("Kode Matakuliah Prodi:", ", ".join(mk_kode_list) or "(-)")

    print("\n--- Rata-rata Nilai Mahasiswa yang Relevan ---")
    
    for m in semua_mahasiswa:
        # Filter nilai yang relevan dengan mata kuliah di prodi ini
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        
        if relevan:
            # Hitung rata-rata
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg, 2)} (Berdasarkan {len(relevan)} nilai)")
        else:
            print(f"  {m.nim} - {m.nama}: (-) (Tidak ada nilai relevan)")
    
    print("-" * 40)

# =================================================================
# CONTOH PENGGUNAAN UTAMA (IMPLEMENTASI LANGKAH a - g)
# =================================================================

if __name__ == "__main__":
    # Inisialisasi dari contoh sebelumnya
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    
    # Inisialisasi Mahasiswa dari contoh sebelumnya
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # Nilai Mhs dari contoh sebelumnya
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))

    # Matakuliah dari contoh sebelumnya
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    # --- Tambahkan 2 Program Studi Baru ---
    prodi_ak = uni.buat_program("Akuntansi")
    prodi_man = uni.buat_program("Manajemen")

    # --- Tambahkan minimal 2 Mata Kuliah ---
    mk3 = MataKuliah("AK301", "Pengantar Akuntansi")
    mk4 = MataKuliah("AK302", "Pajak")
    prodi_ak.tambah_matakuliah(mk3)
    prodi_ak.tambah_matakuliah(mk4)

    mk5 = MataKuliah("MN401", "Manajemen Keuangan")
    mk6 = MataKuliah("MN402", "Pemasaran Digital")
    prodi_man.tambah_matakuliah(mk5)
    prodi_man.tambah_matakuliah(mk6)

    # --- Buat 3 Mahasiswa & Nilai ---
    m3 = Mahasiswa("23003", "Ahmad")
    
    # Tambah Nilai Mhs1 (Budi)
    m1.tambah_nilai(Nilai("AK301", 95)) # Budi ambil Akuntansi
    
    # Tambah Nilai Mhs2 (Siti)
    m2.tambah_nilai(Nilai("MN401", 80)) # Siti ambil Manajemen
    
    # Tambah Nilai Mhs3 (Ahmad)
    m3.tambah_nilai(Nilai("TI101", 70))
    m3.tambah_nilai(Nilai("MN402", 85))
    m3.tambah_nilai(Nilai("AK302", 75))

    semua_mahasiswa = [m1, m2, m3]
    semua_prodi = uni.programs # List semua Program Studi

    print("=" * 60)
    print("DEMO PENGUJIAN SEMUA PROGRAM STUDI DAN MAHASISWA")
    print("=" * 60)

    # --- Tampilkan daftar matkul per Prodi ---
    print("\n[d] Daftar Mata Kuliah per Program Studi:")
    for prodi in semua_prodi:
        mk_kode_list = ", ".join([mk.kode for mk in prodi.daftar_matakuliah])
        print(f"  {prodi.nama}: {mk_kode_list}")

    # --- Tampilkan daftar nilai dan rata-rata global ---
    print("\n[e & f] Daftar Nilai & Rata-rata Global Setiap Mahasiswa:")
    for m in semua_mahasiswa:
        nilai_str = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai])
        print(f"  {m.nama} ({m.nim})")
        print(f"    Nilai: [{nilai_str}]")
        print(f"    Rata-rata Global: {round(m.rata_rata(), 2)}")

    # --- Panggil report_program untuk setiap Prodi ---
    print("\n[g] Laporan Rata-rata Nilai berdasarkan Program Studi (Relevansi):")
    for prodi in semua_prodi:
        report_program(prodi, semua_mahasiswa)