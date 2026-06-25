import csv
import os

class Barang:
    def __init__(self, id_barang, nama, stok, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.stok = int(stok)
        self.harga = float(harga)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_awal(self, id_barang, nama, stok, harga):
        barang_baru = Barang(id_barang, nama, stok, harga)
        barang_baru.next = self.head
        self.head = barang_baru

    def tampilkan_data(self):
        temp = self.head
        if not temp:
            print("Data barang kosong.")
            return False
        print("-" * 55)
        print(f"{'ID':<10} | {'Nama Barang':<20} | {'Stok':<8} | {'Harga':<10}")
        print("-" * 55)
        while temp:
            print(f"{temp.id_barang:<10} | {temp.nama:<20} | {temp.stok:<8} | {temp.harga:<10}")
            temp = temp.next
        print("-" * 55)
        return True

    def cari_barang(self, id_barang):
        temp = self.head
        while temp:
            if temp.id_barang == id_barang:
                return temp
            temp = temp.next
        return None

    def hapus_barang(self, id_barang):
        temp = self.head

        if temp is not None:
            if temp.id_barang == id_barang:
                self.head = temp.next
                temp = None
                return True

        prev = None
        while temp is not None:
            if temp.id_barang == id_barang:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        temp = None
        return True

    def to_list(self):
        arr = []
        temp = self.head
        while temp:
            arr.append([temp.id_barang, temp.nama, temp.stok, temp.harga])
            temp = temp.next
        return arr

class Queue:
    def __init__(self):
        self.antrean = []

    def enqueue(self, item):
        self.antrean.append(item)

    def dequeue(self):
        if len(self.antrean) < 1:
            return None
        return self.antrean.pop(0)

    def tampilkan_antrean(self):
        if not self.antrean:
            print("Antrean kosong.")
        else:
            print("Antrean Keluar Barang:")
            for index, item in enumerate(self.antrean):
                print(f"{index + 1}. {item}")

# Fungsi Database CSV
def muat_data_csv(nama_file, linked_list):
    if not os.path.exists(nama_file):
        return
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader) # Lewati header
        for row in reader:
            if row:
                linked_list.tambah_awal(row[0], row[1], row[2], row[3])

def simpan_data_csv(nama_file, linked_list):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nama", "Stok", "Harga"])
        writer.writerows(linked_list.to_list())

# --- MAIN PROGRAM ---
def main():
    DB_FILE = 'inventori.csv'
    daftar_barang = LinkedList()
    antrean_keluar = Queue()

    muat_data_csv(DB_FILE, daftar_barang)

    while True:
        print("\n=== APLIKASI MANAJEMEN GUDANG ===")
        print("1. Tampilkan Barang (Read)")
        print("2. Tambah Barang (Create)")
        print("3. Update Barang (Update)")
        print("4. Hapus Barang (Delete)")
        print("5. Kelola Antrean Keluar (Queue)")
        print("6. Simpan & Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            daftar_barang.tampilkan_data()

        elif pilihan == '2':
            id_brg = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            stok = input("Masukkan Stok: ")
            harga = input("Masukkan Harga: ")
            daftar_barang.tambah_awal(id_brg, nama, stok, harga)
            print("Barang berhasil ditambahkan!")

        elif pilihan == '3':
            id_brg = input("Masukkan ID Barang yang akan di-update: ")
            barang = daftar_barang.cari_barang(id_brg)
            if barang:
                print(f"Ditemukan: {barang.nama} (Stok: {barang.stok})")
                barang.nama = input("Nama Baru (Enter untuk lewati): ") or barang.nama
                barang.stok = int(input("Stok Baru (Enter untuk lewati): ") or barang.stok)
                barang.harga = float(input("Harga Baru (Enter untuk lewati): ") or barang.harga)
                print("Data berhasil diupdate!")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == '4':
            id_brg = input("Masukkan ID Barang yang akan dihapus: ")
            if daftar_barang.hapus_barang(id_brg):
                print("Barang berhasil dihapus dari sistem.")
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == '5':
            print("\n1. Tambah Antrean Keluar")
            print("2. Proses Antrean (Dequeue)")
            print("3. Lihat Antrean")
            sub_pilih = input("Pilih (1-3): ")
            
            if sub_pilih == '1':
                item = input("Nama Barang yang akan dikeluarkan: ")
                antrean_keluar.enqueue(item)
                print("Ditambahkan ke antrean.")
            elif sub_pilih == '2':
                diproses = antrean_keluar.dequeue()
                if diproses:
                    print(f"Berhasil memproses: {diproses}")
                else:
                    print("Antrean kosong.")
            elif sub_pilih == '3':
                antrean_keluar.tampilkan_antrean()

        elif pilihan == '6':
            simpan_data_csv(DB_FILE, daftar_barang)
            print("Data tersimpan. Terima kasih!")
            break

if __name__ == "__main__":
    main()