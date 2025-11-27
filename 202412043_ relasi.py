# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = [] # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = [] # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)

# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# relasi association
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    
    mk_kode_list = [mk.kode for mk in prodi.daftar_matakuliah]
    print("Matakuliah:", ", ".join(mk_kode_list) or "(-)")

    print("Mahasiswa dan rata-rata nilai:")
    
    for m in semua_mahasiswa:
        # Filter nilai yang relevan dengan mata kuliah di prodi ini
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        
        if relevan:
            # Hitung rata-rata
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
    
    print("-" * 40)

if __name__ == "__main__":
    uni = Universitas("Universitas A")
    
    # Composition: Prodi dibuat oleh Universitas, jika Uni hilang, Prodi biasanya hilang.
    prodi_ti = uni.buat_program("Teknik Informatika")

    # Aggregation: Mata Kuliah dapat ada tanpa Prodi
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)
    
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # Association/Aggregation: Mahasiswa dan Nilai
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))
    # m2 tidak punya nilai untuk TI102 (Struktur Data)

    report_program(prodi_ti, [m1, m2])