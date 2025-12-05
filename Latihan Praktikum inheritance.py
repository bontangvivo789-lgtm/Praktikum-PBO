# Buat class Person dengan atribut nama dan umur.
class Person:
    # Constructor untuk inisialisasi atribut
    def __init__(self, nama, umur):
        self.nama = nama  # Atribut nama
        self.umur = umur  # Atribut umur

    # Method untuk menampilkan informasi
    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"

# Buat class Mahasiswa yang mewarisi Person, tambahkan atribut nim.
class Mahasiswa(Person):
    # Constructor untuk inisialisasi atribut
    def __init__(self, nama, umur, nim):
        # Gunakan super() untuk inisialisasi atribut dari parent class (Person)
        super().__init__(nama, umur)
        self.nim = nim  # Atribut tambahan untuk Mahasiswa

    # Override method info() dari parent class
    def info(self):
        # Menggabungkan informasi dari parent dan child class
        return f"Mahasiswa: {self.nama}, NIM: {self.nim}, Umur: {self.umur} tahun"

# Instansiasi objek dan panggil method info().
# Instansiasi objek dari class Person
p1 = Person("Surya", 30)

# Instansiasi objek dari class Mahasiswa
m1 = Mahasiswa("Galang", 20, "202412043")

# Panggil method info() pada objek Person
print("--- Info Person ---")
print(p1.info())

# Panggil method info() pada objek Mahasiswa
print("\n--- Info Mahasiswa ---")
print(m1.info())