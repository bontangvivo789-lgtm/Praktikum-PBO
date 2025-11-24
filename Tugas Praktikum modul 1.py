class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Instance attributes
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        print(f"Hallo, nama saya {self.nama}, NIM {self.nim}.")
        print(f"Saya dari jurusan {self.jurusan}.")
        print(f"Universitas: {Mahasiswa.universitas}\n")

    # Method update IPK
    def update_ipk(self, ipk_baru):
        print(f"IPK lama: {self.ipk}")
        self.ipk = ipk_baru
        print(f"IPK baru berhasil diperbarui menjadi: {self.ipk}\n")

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# ---------------------------------------------------------
#                 INSTANSIASI OBJEK
# ---------------------------------------------------------

# Membuat 3 objek mahasiswa
mhs1 = Mahasiswa("Galang", "202412044", "Informatika", 3.6)
mhs2 = Mahasiswa("Surya", "202412045", "Sistem Informasi", 3.1)
mhs3 = Mahasiswa("Nata", "202412043", "Teknik Industri", 2.4)
mhs4 = Mahasiswa("Paijo", "202412042", "Perikanan", 2.0)
# Menampilkan semua method
print("=== DATA MAHASISWA 1 ===")
mhs1.perkenalan_diri()
print("Predikat Kelulusan:", mhs1.predikat_kelulusan(), "\n")

print("=== DATA MAHASISWA 2 ===")
mhs2.perkenalan_diri()
print("Predikat Kelulusan:", mhs2.predikat_kelulusan(), "\n")

print("=== DATA MAHASISWA 3 ===")
mhs3.perkenalan_diri()
print("Predikat Kelulusan:", mhs3.predikat_kelulusan(), "\n")

print("=== DATA MAHASISWA 4 ===")
mhs4.perkenalan_diri()
print("Predikat Kelulusan:", mhs4.predikat_kelulusan(), "\n")

# Update IPK contoh
mhs3.update_ipk(2.8)
print("Predikat Setelah Update:", mhs3.predikat_kelulusan())
