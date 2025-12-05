class Burung:
    def terbang(self):
        return "Burung terbang tinggi"

class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"

def uji_terbang(obj):
    # Method ini akan bekerja selama objek memiliki method 'terbang()'
    print(obj.terbang())

# Duck Typing dalam aksi
b = Burung()
p = Pesawat()

uji_terbang(b)
uji_terbang(p)