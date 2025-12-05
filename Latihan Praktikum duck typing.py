# Dua class berbeda (Laptop, Smartphone) dengan method nyalakan().
class Laptop:
    def nyalakan(self):
        return "Laptop menyala, menampilkan desktop."

class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala, menampilkan lock screen."

# Fungsi tes_nyala(obj) yang memanggil method nyalakan().
def tes_nyala(obj):
    print(obj.nyalakan())

# Demonstrasikan duck typing
print("\n--- Duck Typing (Nyalakan) ---")
tes_nyala(Laptop())
tes_nyala(Smartphone())