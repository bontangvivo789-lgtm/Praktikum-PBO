class Kendaraan:
    # Atribut ini sama untuk semua instance (objek) dari kelas Kendaraan
    bahan_bakar = "Bensin"

    # Gunakan constructor untuk inisialisasi merk, warna, dan tahun
    def __init__(self, merk, warna, tahun):
        """
        Konstruktor untuk menginisialisasi Instance Attributes (unik per objek).
        """
        self.merk = merk    # Instance Attribute
        self.warna = warna  # Instance Attribute
        self.tahun = tahun  # Instance Attribute

    def info_kendaraan(self):
        """
        Metode untuk menampilkan semua informasi Instance Attribute.
        """
        return f"{self.merk} berwarna {self.warna}, tahun {self.tahun}."

    def info_lengkap(self):
        """
        Metode yang menggabungkan Instance Attribute dan Class Attribute.
        """
        # Akses Class Attribute melalui nama Class (Kendaraan.bahan_bakar)
        return f"{self.info_kendaraan()} Menggunakan bahan bakar {Kendaraan.bahan_bakar}."


# Demonstrasikan perbedaan akses instance attribute dan class attribute ---

# 1. Instansiasi 2 objek Kendaraan (membuat Instance)
mobil1 = Kendaraan("Toyota", "Merah", 2020)
mobil2 = Kendaraan("Honda", "Putih", 2022)
print("--- 1. Akses Instance Attributes (Unik per Objek) ---")

# Akses Instance Attributes menggunakan nama objek (Instance)
print(f"Merk mobil 1: {mobil1.merk}")
print(f"Warna mobil 2: {mobil2.warna}")
print(f"Info lengkap mobil 1: {mobil1.info_lengkap()}")
print("\n--- 2. Akses Class Attribute (Sama untuk semua) ---")

# Akses Class Attribute melalui nama Class itu sendiri (cara yang direkomendasikan)
print(f"Bahan Bakar default (via Class): {Kendaraan.bahan_bakar}")

# Class Attribute juga bisa diakses melalui objek, tapi sebenarnya tetap merujuk ke Class
print(f"Bahan Bakar mobil 1 (via Instance): {mobil1.bahan_bakar}")
print(f"Bahan Bakar mobil 2 (via Instance): {mobil2.bahan_bakar}")
print("\n--- 3. Modifikasi Class Attribute (Memengaruhi Semua Objek) ---")

# Jika kita mengubah Class Attribute, itu akan memengaruhi semua objek
Kendaraan.bahan_bakar = "Listrik"
print(f"Bahan Bakar default BARU: {Kendaraan.bahan_bakar}")
print(f"Info lengkap mobil 2 setelah diubah: {mobil2.info_lengkap()}")