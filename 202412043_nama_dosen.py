## 🎓 Implementasi Class Dosen
class Dosen:
    # a. Buat class Dosen dengan atribut nama dan nidn
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya Dosen {self.nama} dengan NIDN {self.nidn}."

    # b. Tambahkan method ajar_mata_kuliah()
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) sedang mengajar mata kuliah: {mata_kuliah}"

# --- c. Instansiasi 2 object dosen dan panggil methodnya ---

# Instansiasi 2 object Dosen
dosen1 = Dosen("Ir. Abadi Nugroho, S.Kom., M.Kom.", "1104129002")
dosen2 = Dosen("Herri Susanto, S.S., M.Hum", "1118097701")

print("--- Hasil Instansiasi Objek ---")
print(dosen1.perkenalan())
print(dosen2.perkenalan())

print("\n--- Pemanggilan Method ajar_mata_kuliah() ---")
# Panggil method ajar_mata_kuliah pada masing-masing objek
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Keterampilan Komunikasi"))