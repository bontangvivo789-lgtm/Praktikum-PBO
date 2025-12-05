# Class Parent: Karyawan (Base Class)
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    # Method: info_gaji()
    def info_gaji(self):
        """Menampilkan informasi gaji pokok karyawan."""
        return f"Gaji Pokok: Rp{self.gaji_pokok:,.0f}"

    def __str__(self):
        return f"{self.__class__.__name__} - Nama: {self.nama}"

# --- Inheritance ---

# Child Class: Manager (inherits Karyawan)
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        # Memanggil konstruktor Parent Class
        super().__init__(nama, gaji_pokok)
        # Atribut tambahan: tunjangan
        self.tunjangan = tunjangan

    # Override method info_gaji()
    def info_gaji(self):
        """Menampilkan gaji total (gaji_pokok + tunjangan)."""
        gaji_total = self.gaji_pokok + self.tunjangan
        return f"Gaji Total Manager ({self.nama}): Rp{gaji_total:,.0f} (Pokok: Rp{self.gaji_pokok:,.0f} + Tunjangan: Rp{self.tunjangan:,.0f})"

# Child Class: Programmer (inherits Karyawan)
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        # Memanggil konstruktor Parent Class
        super().__init__(nama, gaji_pokok)
        # Atribut tambahan: bonus
        self.bonus = bonus

    # Override method info_gaji()
    def info_gaji(self):
        """Menampilkan gaji total (gaji_pokok + bonus)."""
        gaji_total = self.gaji_pokok + self.bonus
        return f"Gaji Total Programmer ({self.nama}): Rp{gaji_total:,.0f} (Pokok: Rp{self.gaji_pokok:,.0f} + Bonus: Rp{self.bonus:,.0f})"

# Composition: Class Departemen
class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        # Komposisi: Memiliki daftar objek karyawan (list of objects)
        self.daftar_karyawan = []

    # Method: tambah_karyawan(karyawan)
    def tambah_karyawan(self, karyawan):
        """Menambahkan objek karyawan ke dalam departemen."""
        self.daftar_karyawan.append(karyawan)
        print(f" {karyawan.nama} telah ditambahkan ke Departemen {self.nama_dept}")

    # Method: tampilkan_karyawan()
    def tampilkan_karyawan(self):
        """Menampilkan info gaji untuk semua karyawan dalam departemen."""
        print(f"\n--- Info Gaji Karyawan Departemen {self.nama_dept} ---")
        if not self.daftar_karyawan:
            print("Belum ada karyawan.")
            return

        for karyawan in self.daftar_karyawan:
            # Polymorphism: Setiap objek akan memanggil info_gaji() versi kelasnya sendiri
            print(f"* {karyawan.info_gaji()}")

# Instansiasi: Buat 2 Manager dan 2 Programmer
manager1 = Manager("Galang", 8000000, 2000000)
manager2 = Manager("Surya", 9000000, 2500000)
programmer1 = Programmer("Nata", 6500000, 1000000)
programmer2 = Programmer("Budi", 7000000, 1200000)

# Instansiasi Departemen
dept_it = Departemen("Teknologi Informasi")

# Tambahkan ke dalam departemen
dept_it.tambah_karyawan(manager1)
dept_it.tambah_karyawan(manager2)
dept_it.tambah_karyawan(programmer1)
dept_it.tambah_karyawan(programmer2)

# Tampilkan info gaji semua karyawan
dept_it.tampilkan_karyawan()

print("\n--- Info Gaji Karyawan Biasa (Parent Class) ---")
karyawan_biasa = Karyawan("Eko", 5000000)
print(f"* {karyawan_biasa.info_gaji()}")