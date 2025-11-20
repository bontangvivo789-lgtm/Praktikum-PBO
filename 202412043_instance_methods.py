## Implementasi Class ManajerInventori
class ManajerInventori:
    def __init__(self):
        # Data inventori disimpan dalam bentuk dictionary: {nama_barang: stok}
        self.stok = {}

    # Method tambah_barang
    def tambah_barang(self, nama_barang, jumlah):
        # Implementasi penambahan stok
        if nama_barang in self.stok:
            # Jika barang sudah ada, tambahkan stok
            self.stok[nama_barang] += jumlah
            return f"Stok {nama_barang} berhasil ditambah {jumlah}. Total stok: {self.stok[nama_barang]}"
        else:
            # Jika barang belum ada, tambahkan item baru
            self.stok[nama_barang] = jumlah
            return f"Barang baru {nama_barang} ditambahkan dengan stok awal: {jumlah}"

    # Method hapus_barang
    def hapus_barang(self, nama_barang, jumlah):
        # Implementasi pengurangan stok
        if nama_barang not in self.stok:
            return f"Gagal: Barang {nama_barang} tidak ditemukan di inventori."

        if jumlah > self.stok[nama_barang]:
            return f"Gagal: Pengurangan {jumlah} melebihi stok yang ada ({self.stok[nama_barang]}) untuk barang {nama_barang}."
        
        # Kurangi stok
        self.stok[nama_barang] -= jumlah

        if self.stok[nama_barang] == 0:
            # Opsional: Hapus barang dari dictionary jika stoknya habis
            del self.stok[nama_barang]
            return f"Stok {nama_barang} berkurang {jumlah}. Stok habis dan item dihapus dari inventori."
        else:
            return f"Stok {nama_barang} berhasil dikurangi {jumlah}. Sisa stok: {self.stok[nama_barang]}"

    # Method lihat_inventori
    def lihat_inventori(self):
        """
        Menampilkan semua barang dan stok yang ada.
        """
        if not self.stok:
            return "Inventori kosong."
        
        output = "\n--- Laporan Inventori ---\n"
        for barang, jumlah in self.stok.items():
            output += f"- {barang}: {jumlah} unit\n"
        return output


# Demonstrasi semua method yang telah dibuat ---

# Instansiasi objek ManajerInventori
manajer = ManajerInventori()

print("== 1. Demo Penambahan Barang ==")
print(manajer.tambah_barang("Laptop", 10))
print(manajer.tambah_barang("Monitor", 5))
print(manajer.tambah_barang("Laptop", 3)) # Menambah stok yang sudah ada
print("-" * 30)

print("== 2. Demo Melihat Inventori ==")
print(manajer.lihat_inventori())
print("-" * 30)

print("== 3. Demo Pengurangan Barang (Berhasil) ==")
print(manajer.hapus_barang("Monitor", 2))
print("-" * 30)

print("== 4. Demo Pengurangan Barang (Gagal: Stok tidak cukup) ==")
print(manajer.hapus_barang("Laptop", 50))
print("-" * 30)

print("== 5. Demo Pengurangan Barang (Stok habis) ==")
print(manajer.hapus_barang("Monitor", 3))
print("-" * 30)

print("== 6. Demo Inventori Akhir ==")
print(manajer.lihat_inventori())