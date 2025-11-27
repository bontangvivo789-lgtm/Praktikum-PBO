class Mahasiswa:
    """Kelas untuk merepresentasikan objek Mahasiswa."""
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class MataKuliah:
    """Kelas untuk merepresentasikan objek Mata Kuliah yang memiliki daftar Mahasiswa."""
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = [] # List untuk menyimpan objek Mahasiswa

    def tambah_mahasiswa(self, mhs):
        """Menambahkan objek Mahasiswa ke dalam list."""
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        """Mengembalikan list nama mahasiswa."""
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        """Mengembalikan jumlah total mahasiswa yang terdaftar."""
        return len(self.mahasiswa)
    
class Student:
    """Kelas Student untuk mengelola data GPA dan Credit."""
    def __init__(self, sid, name, gpa=0.0):
        self.sid = sid          # public
        self.name = name        # public
        self._credits = 0       # protected (Menggunakan satu underscore)
        self.__gpa = gpa        # private (Menggunakan double underscore)

    def get_gpa(self):
        """Mengembalikan nilai GPA."""
        return self.__gpa

    def set_gpa(self, value):
        """Mengatur nilai GPA dengan validasi."""
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA harus antara 0.0 dan 4.0")
        self.__gpa = round(value, 2)

    def add_credits(self, n):
        """Menambahkan credit dengan validasi."""
        if n < 0:
            raise ValueError("credits tidak boleh negatif")
        self._credits += n

    def classify(self):
        """Mengembalikan klasifikasi berdasarkan nilai GPA."""
        gpa = self.__gpa
        if gpa >= 3.5:
            return "Cum Laude"
        elif gpa >= 2.5:
            return "Good"
        else:
            return "Remedial"

if __name__ == "__main__":
    print("===== DEMO KELAS STUDENT (GPA/CLASSIFY) =====")
    
    # Inisialisasi Student
    s = Student("S100", "Ana", 3.1)
    
    print(f"Nama Student: {s.name}")
    print(f"GPA Awal: {s.get_gpa()} ({s.classify()})") # Output: 3.1 (Good)
    
    # Update GPA dan Credits
    s.set_gpa(3.75)
    s.add_credits(3)
    
    print(f"GPA Baru: {s.get_gpa()} ({s.classify()})") # Output: 3.75 (Cum Laude)
    print(f"Total Credits: {s._credits}")            # Output: 3
    
    print("\n===== DEMO KELAS MATA KULIAH (RELASI) =====")
    
    # 1. Buat Mata Kuliah
    mk_pd = MataKuliah("TI101", "Pemrograman Dasar")
    mk_dsa = MataKuliah("TI205", "Struktur Data")
    
    # 2. Buat Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Ahmad")
    
    # 3. Daftarkan Mahasiswa
    mk_pd.tambah_mahasiswa(m1) 
    mk_pd.tambah_mahasiswa(m2) 
    
    mk_dsa.tambah_mahasiswa(m2) 
    mk_dsa.tambah_mahasiswa(m3) 
    mk_dsa.tambah_mahasiswa(m1) 
    
    # 4. Tampilkan Hasil
    print("-----------------------------------------")
    print(f"Mata Kuliah: {mk_pd.nama}")
    print(f"Daftar Mhs: {mk_pd.daftar_mahasiswa()}")
    print(f"Jumlah Mhs: {mk_pd.jumlah_mahasiswa()}")
    
    print("-----------------------------------------")
    print(f"Mata Kuliah: {mk_dsa.nama}")
    print(f"Daftar Mhs: {mk_dsa.daftar_mahasiswa()}")
    print(f"Jumlah Mhs: {mk_dsa.jumlah_mahasiswa()}")
    print("-----------------------------------------")