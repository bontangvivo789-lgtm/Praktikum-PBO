class Mahasiswa:
    def __init__(self, nim, nama, semester, IPK):
        # Public Attributes
        self.nim = nim
        self.nama = nama
        
        # Protected Attribute (diawali satu underscore)
        self._semester = semester
        
        # Private Attribute (diawali dua underscore)
        self.__IPK = IPK

    def get_ipk(self):
        """Getter untuk IPK (Private)"""
        return self.__IPK

    def set_ipk(self, nilai_baru):
        """Setter untuk IPK (Private) dengan validasi"""
        if not (0.0 <= nilai_baru <= 4.0):
            raise ValueError("Nilai IPK harus antara 0.0 dan 4.0.")
        self.__IPK = nilai_baru

    def get_semester(self):
        """Getter untuk semester (Protected)"""
        return self._semester
    
    def set_semester(self, nilai_baru):
        """Setter untuk semester (Protected) dengan validasi"""
        if nilai_baru < 1:
            raise ValueError("Semester tidak boleh kurang dari 1.")
        self._semester = nilai_baru


if __name__ == "__main__":
    # a. Buat 2 objek Mahasiswa
    mhs1 = Mahasiswa("12345", "Budi Santoso", 3, 3.85)
    mhs2 = Mahasiswa("67890", "Citra Dewi", 5, 3.10)

    # ==================================================
    # b. Tampilkan data awal:
    # ==================================================
    print("====================== DATA AWAL ======================")
    
    # Mhs1: Public diakses langsung, Protected/Private diakses via Getter
    print(f"Mahasiswa 1: {mhs1.nama}")
    print(f"  NIM (Public): {mhs1.nim}")
    print(f"  Semester (Protected): {mhs1.get_semester()}")
    print(f"  IPK (Private): {mhs1.get_ipk()}")
    
    # Mhs2:
    print(f"\nMahasiswa 2: {mhs2.nama}")
    print(f"  NIM (Public): {mhs2.nim}")
    print(f"  Semester (Protected): {mhs2.get_semester()}")
    print(f"  IPK (Private): {mhs2.get_ipk()}")

    mhs1.set_semester(4)
    mhs1.set_ipk(3.95) 
    mhs2._semester = 6
    mhs2.set_ipk(3.25)
    
    print("\n=================== DATA SETELAH UPDATE ===================")
    print(f"Mahasiswa 1: {mhs1.nama}")
    print(f"  Semester Baru: {mhs1.get_semester()}") # Output: 4
    print(f"  IPK Baru: {mhs1.get_ipk()}")           # Output: 3.95
    
    print(f"\nMahasiswa 2: {mhs2.nama}")
    print(f"  Semester Baru: {mhs2.get_semester()}") # Output: 6
    print(f"  IPK Baru: {mhs2.get_ipk()}")           # Output: 3.25
    print("=========================================================")