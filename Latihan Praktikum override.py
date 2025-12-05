import math
# Class Bentuk dengan method luas() yang mengembalikan 0.
class Bentuk:
    def luas(self):
        # Implementasi default/kosong
        return 0

# Class Persegi yang meng-override method luas().
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    # Meng-override method luas() untuk menghitung luas Persegi
    def luas(self):
        return self.sisi * self.sisi

# Class Lingkaran yang meng-override method luas().
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    # Meng-override method luas() untuk menghitung luas Lingkaran
    def luas(self):
        # Luas Lingkaran = pi * r^2
        return math.pi * (self.radius ** 2)

# Demonstrasikan pemanggilan method luas() dari objek masing-masing class.
# Instansiasi objek
b_obj = Bentuk()
p_obj = Persegi(sisi=4)
l_obj = Lingkaran(radius=5)

# Panggil method luas()
print(f"Luas Bentuk (default): {b_obj.luas()}")
print(f"Luas Persegi (sisi=4): {p_obj.luas()}")
print(f"Luas Lingkaran (r=5): {l_obj.luas():.2f}") # Dibulatkan 2 desimal