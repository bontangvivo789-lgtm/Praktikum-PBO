class Hewan:
    def bersuara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def bersuara(self):
        return "Meow!"

class Anjing(Hewan):
    def bersuara(self):
        return "Woof!"

# Polimorfisme dalam aksi
hewan_list = [Hewan(), Kucing(), Anjing()]

for h in hewan_list:
    print(h.bersuara())